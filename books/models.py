from django.db import models
from django.db.models import Max, Min
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from core.constants import LANGUAGES, FORMATS, DEGREE, GENDER, CONTENT_RATING, ROLE
from core.models import AbstractImage


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = _('Publisher')
        verbose_name_plural = _('Publishers')

    def __str__(self):
        return self.name


class Author(models.Model):
    goodreads_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100)
    influences = models.ForeignKey('self', null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, default=0, blank=True)
    hometown = models.CharField(max_length=100, blank=True)
    born_at = models.DateField(null=True, blank=True)
    died_at = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def get_photo(self):
        return self.authorphoto_set.get(primary=True)


class AuthorPhoto(AbstractImage, models.Model):
    author = models.ForeignKey(Author)
    primary = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Author Photos')
        verbose_name_plural = _('Authors Photos')

    def __str__(self):
        return self.author.name

    def save(self, *args, **kwargs):
        if self.primary:
            try:
                old_prim = AuthorPhoto.objects.get(primary=True, author=self.author)
                old_prim.primary = False
                old_prim.save(update_fields=['primary'])
            except self.DoesNotExist:
                pass
        super(AuthorPhoto, self).save(*args, **kwargs)


class Series(models.Model):
    goodreads_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=400)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = _('Series')
        verbose_name_plural = _('Series')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('series-detail', args=[str(self.id)])


class Genres(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    fb2_code = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')

    def __str__(self):
        return self.title


class BookGenres(models.Model):
    book = models.ForeignKey('Book')
    genres = models.ForeignKey(Genres)
    communications_degree = models.IntegerField(choices=DEGREE, default=5)


class Book(models.Model):
    work_id = models.IntegerField(null=True, blank=True)
    original_title = models.CharField(max_length=400)
    description = models.TextField(blank=True)
    genres = models.ManyToManyField(Genres, through=BookGenres)
    content_rating = models.IntegerField(choices=CONTENT_RATING, default=0)
    original_publication_date = models.DateField(null=True, blank=True)
    edition = []

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return self.original_title

    def get_absolute_url(self):
        return reverse('book-summary', args=[str(self.id)])

    def get_editions(self):
        self.edition = self.edition_set.all()
        return self.edition

    def get_authors(self):
        return self.editionauthor_set.all() \
            .select_related('author',
                            'edition',
                            'book') \
            .order_by('author') \
            .distinct('author')

    def get_series(self):
        return self.editionseries_set.all() \
            .select_related('series',
                            'edition',
                            'book') \
            .order_by('series') \
            .distinct('series')

    def get_lang(self):
        return list(set([x.get_language_display() for x in self.edition]))[:2]

    def get_format(self):
        return list(set([x.get_book_format_display() for x in self.edition]))[:2]

    def get_cover(self):
        for x in self.edition:
            if x.is_original:
                try:
                    return x.image.url
                except ValueError:
                    pass

    def get_pages(self):
        return self.edition.distinct().aggregate(min=Min('num_pages'), max=Max('num_pages'))  # notice +1 запрос


class CoverOfPublisher(AbstractImage, models.Model):
    description = models.TextField(blank=True)
    publisher = models.ForeignKey(Publisher)


class Edition(AbstractImage, models.Model):
    goodreads_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=400)
    description = models.TextField(blank=True)
    language = models.CharField(choices=LANGUAGES, default='unknown', max_length=10, blank=True)
    isbn = models.CharField(max_length=11, blank=True)
    isbn13 = models.CharField(max_length=14, blank=True)
    asin = models.CharField(max_length=100, blank=True)
    kindle_asin = models.CharField(max_length=100, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    num_pages = models.IntegerField(null=True, blank=True)
    book_format = models.IntegerField(choices=FORMATS, default=0)
    is_ebook = models.BooleanField()
    is_original = models.BooleanField(default=False)
    publisher = models.ForeignKey(Publisher, null=True, blank=True)
    author = models.ManyToManyField(Author, through='EditionAuthor')
    series = models.ManyToManyField(Series, through='EditionSeries', blank=True)
    summary = models.ForeignKey(Book)

    class Meta:
        verbose_name = _('Edition')
        verbose_name_plural = _('Editions')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.publication_date < self.summary.original_publication_date:
            self.is_original = True
            b = self.summary
            b.original_publication_date = self.publication_date
            b.save(update_fields=['original_publication_date'])
        if self.is_original:
            try:
                old_prim = Edition.objects.get(is_original=True, summary=self.summary)
                if old_prim != self:
                    old_prim.is_original = False
                    old_prim.save(update_fields=['is_original'])
                    self.is_original = True
            except Edition.DoesNotExist:
                self.is_original = True
        else:
            try:
                Edition.objects.get(is_original=True, summary=self.summary)
            except Edition.DoesNotExist:
                self.is_original = True
        super(Edition, self).save(*args, **kwargs)


class EditionSeries(models.Model):
    edition = models.ForeignKey(Edition)
    series = models.ForeignKey(Series)
    book = models.ForeignKey(Book, blank=True)
    position = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.book = self.edition.summary
        super(EditionSeries, self).save(*args, **kwargs)


class EditionAuthor(models.Model):
    edition = models.ForeignKey(Edition)
    author = models.ForeignKey(Author)
    book = models.ForeignKey(Book)
    role = models.IntegerField(choices=ROLE, default=1)
