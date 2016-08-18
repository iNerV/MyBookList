from django.db import models
from django.db.models import Max, Min
from django.db.models.deletion import SET_NULL

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from books.utils import convert_10_to_13

from core.constants import LANGUAGES, FORMATS, DEGREE, GENDER, CONTENT_RATING, ROLE, PLOT_STRUCTURES, TIME_OF_ACTION
from core.mixins import AbstractBilingual, AbstractImage


class Publisher(models.Model):
    name = models.CharField(max_length=400)
    description_ru = models.TextField(blank=True)
    description_eng = models.TextField(blank=True)

    class Meta:
        verbose_name = _('Издатель')
        verbose_name_plural = _('Издатели')

    def __str__(self):
        return self.name


class CoverOfPublisher(AbstractImage, models.Model):
    publisher = models.ForeignKey(Publisher)


class Author(AbstractBilingual, models.Model):
    goodreads_id = models.IntegerField(null=True, blank=True)
    influences = models.ForeignKey('self', null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, default=0, blank=True)
    hometown = models.CharField(max_length=100, blank=True)
    born_at = models.DateField(null=True, blank=True)
    died_at = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = _('Автор')
        verbose_name_plural = _('Авторы')

    def __str__(self):
        return self.name_eng

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})

    def get_photo(self):
        return self.authorphoto_set.get(primary=True)


class AuthorPhoto(AbstractImage, models.Model):
    author = models.ForeignKey(Author)
    primary = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Фотография автора')
        verbose_name_plural = _('Фотографии автора')

    def __str__(self):
        return self.author.name_eng

    def clean(self, *args, **kwargs):
        if self.primary:
            AuthorPhoto.objects.filter(primary=True, author=self.author).exclude(pk=self.pk).update(primary=False)
            # try:
            #     old_prim = AuthorPhoto.objects.get(primary=True, author=self.author)
            #     old_prim.primary = False
            #     old_prim.save(update_fields=['primary'])
            # except self.DoesNotExist:
            #     pass
        else:
            try:
                AuthorPhoto.objects.get(primary=True, author=self.author)
            except AuthorPhoto.DoesNotExist:
                self.primary = True


class Series(AbstractBilingual, models.Model):
    goodreads_id = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = _('Серия')
        verbose_name_plural = _('Серии')

    def __str__(self):
        return self.name_eng

    def get_absolute_url(self):
        return reverse('series-detail', kwargs={'pk': self.pk})


class Genre(AbstractBilingual, models.Model):
    fb2_code = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('Жанр')
        verbose_name_plural = _('Жанры')

    def __str__(self):
        return self.name_eng


class Book(AbstractBilingual, models.Model):
    work_id = models.IntegerField(null=True, blank=True)
    content_rating = models.IntegerField(choices=CONTENT_RATING, default=0)
    plot_structures = models.IntegerField(choices=PLOT_STRUCTURES, default=0)
    time_of_action = models.IntegerField(choices=TIME_OF_ACTION, default=0)
    genres = models.ManyToManyField(Genre, through='BookGenres')
    series = models.ManyToManyField(Series, through='BookSeries', blank=True)
    _editions = []

    class Meta:
        verbose_name = _('Книга')
        verbose_name_plural = _('Книги')

    def __str__(self):
        return self.name_eng

    def get_absolute_url(self):
        return reverse('book-summary', kwargs={'pk': self.pk})

    def get_editions(self):
        self._editions = self.edition_set.all()
        return self._editions

    def get_authors(self):
        return self.editionauthor_set.all() \
            .select_related('author',
                            'edition',
                            'book') \
            .order_by('author') \
            .distinct('author')

    def get_series(self):
        return self.bookseries_set.all() \
            .select_related('series',
                            'book') \
            .order_by('series') \
            .distinct('series')

    def get_lang(self):
        return list(set([x.get_language_display() for x in self._editions]))[:2]

    def get_format(self):
        return list(set([x.get_book_format_display() for x in self._editions]))[:2]

    def get_cover(self):
        for x in self._editions:
            if x.is_original:
                try:
                    return x.image.url
                except ValueError:
                    pass

    def get_pages(self):
        return self._editions.distinct().aggregate(min=Min('num_pages'), max=Max('num_pages'))  # notice +1 запрос


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
    is_ebook = models.BooleanField()  # todo подумать над удалением (дублирующая информаиця)
    is_original = models.BooleanField(default=False)
    publisher = models.ForeignKey(Publisher, on_delete=SET_NULL, null=True, blank=True)
    author = models.ManyToManyField(Author, through='EditionAuthor')
    summary = models.ForeignKey(Book, on_delete=SET_NULL, null=True)

    class Meta:
        verbose_name = _('Издание')
        verbose_name_plural = _('Издания')

    def __str__(self):
        return self.title

    def clean(self, *args, **kwargs):  # fixme вернуть в save
        if self.isbn and not self.isbn13:
            self.isbn13 = convert_10_to_13(self.isbn)

        if self.publication_date:
            pub_date = Edition.objects.filter(summary=self.summary, publication_date__lte=self.publication_date)\
                .exclude(pk=self.pk)
            if not pub_date:
                self.is_original = True

        if self.is_original:
            min_pub = Edition.objects.aggregate(min=Min('publication_date'))
            if self.publication_date > min_pub['min'] and min_pub is not None:
                self.is_original = False
            else:
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


class BookGenres(models.Model):
    book = models.ForeignKey(Book)
    genres = models.ForeignKey(Genre)
    communications_degree = models.IntegerField(choices=DEGREE, default=5)


class BookSeries(models.Model):
    series = models.ForeignKey(Series)
    book = models.ForeignKey(Book)
    position = models.CharField(max_length=50)


class EditionAuthor(models.Model):
    edition = models.ForeignKey(Edition)
    author = models.ForeignKey(Author)
    book = models.ForeignKey(Book, blank=True)
    role = models.IntegerField(choices=ROLE, default=1)

    # def save(self, *args, **kwargs):
    #     self.book = self.edition.summary
    #     super(EditionAuthor, self).save(*args, **kwargs)
