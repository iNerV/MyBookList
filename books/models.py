from django.db import models
from django.db.models import Max, Min
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail, delete
from django.core.files.base import ContentFile
from django.core.urlresolvers import reverse

from core.constants import LANGUAGES, FORMATS, DEGREE, GENDER, CONTENT_RATING, ROLE


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def get_photo(self):
        return self.authorphoto_set.get(primary=True)


def author_photo(instance, filename):
    return 'authors/{0}/{1}'.format(instance.author_id, filename)


class AuthorPhoto(models.Model):
    photo = ImageField(upload_to=author_photo)
    author = models.ForeignKey(Author)
    primary = models.BooleanField(default=False)

    def __str__(self):
        return str(self.photo)

    def save(self, *args, **kwargs):
        if self.primary:
            old_prim = AuthorPhoto.objects.get(primary=True, author=self.author)
            old_prim.primary = False
            old_prim.save(update_fields=['primary'])
        super(AuthorPhoto, self).save(*args, **kwargs)


class Series(models.Model):
    goodreads_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=400)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('series-detail', args=[str(self.id)])


class Genres(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    fb2_code = models.CharField(max_length=20)

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
        cover = ''
        for x in self.edition:
            if x.is_original:
                try:
                    cover = x.cover.url
                except ValueError:
                    pass
        return cover

    def get_pages(self):
        return self.edition.distinct().aggregate(min=Min('num_pages'), max=Max('num_pages'))  # notice +1 запрос


def publisher_logo(instance, filename):
    return 'publishers/{0}/{1}'.format(instance.id, filename)


class CoverOfPublisher(models.Model):
    logo = ImageField(upload_to=publisher_logo)
    description = models.TextField(blank=True)
    publisher = models.ForeignKey(Publisher)


def book_cover(instance, filename):
        return 'books/{0}/{1}'.format(instance.summary_id, filename)


class Edition(models.Model):
    goodreads_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=400)
    description = models.TextField(blank=True)
    language = models.CharField(choices=LANGUAGES, default='unknown', max_length=10, blank=True)
    cover = models.ImageField(upload_to=book_cover, blank=True)
    cover_xs = models.ImageField(upload_to=book_cover, blank=True)  # 48
    cover_sm = models.ImageField(upload_to=book_cover, blank=True)  # 96
    cover_md = models.ImageField(upload_to=book_cover, blank=True)  # 120
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

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # if not self.id:
        # super(Edition, self).save(*args, **kwargs)
        # print('test')
        # resized_48 = get_thumbnail(self.cover, '64', crop='center', quality=99)
        # resized_96 = get_thumbnail(self.cover, '96', crop='center', quality=99)
        # resized_120 = get_thumbnail(self.cover, '120', crop='center', quality=99)
        # self.cover_xs.save(resized_48.name, resized_48.read(), True)
        # self.cover_sm.save(resized_96.name, resized_96.read(), True)
        # self.cover_md.save(resized_120.name, resized_120.read(), True)
            # delete(my_file)
        # try:  # error не работает загрузка изображений
        #     Edition.objects.get(is_original=True, summary=self.summary)
        # except Edition.DoesNotExist:
        #     self.is_original = True
        # if self.summary.original_publication_date == self.publication_date:
        #     try:
        #         old_prim = Edition.objects.get(is_original=True, summary=self.summary)
        #         old_prim.is_original = False
        #         old_prim.save(update_fields=['is_original'])
        #         self.is_original = True
        #     except Edition.DoesNotExist:
        #         pass
        # if not self.is_original:
        #     self.is_original = True
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
