from django.test import TestCase

from django.core.exceptions import ValidationError

import datetime

from books.models import *


class BookTestCase(TestCase):
    def setUp(self):
        self.series = Series.objects.create(goodreads_id=1,
                                            name_ru='Серия',
                                            name_eng='Series',
                                            description_ru='Русское описание',
                                            description_eng='English description')
        self.book = Book.objects.create(work_id=1,
                                        content_rating=1,
                                        plot_structures=1,
                                        time_of_action=1,
                                        name_ru='Название',
                                        name_eng='Title',
                                        description_ru='Русское описание',
                                        description_eng='English description')
        self.author = Author.objects.create(goodreads_id=1,
                                            gender=1,
                                            hometown='City_of_test',
                                            born_at='2016-08-11',
                                            died_at='2016-08-11',
                                            name_ru='Имя',
                                            name_eng='Name',
                                            description_ru='Русское описание',
                                            description_eng='English description')
        self.publisher = Publisher.objects.create(description_ru='Русское описание',
                                                  description_eng='English description',
                                                  name='Test publisher')
        self.edition = Edition.objects.create(goodreads_id=1,
                                              title='Test edition 1',
                                              description='test descr',
                                              language='abk',
                                              isbn='0451524934',
                                              isbn13='9780451524935',
                                              asin='0451524934',
                                              kindle_asin='',
                                              publication_date='2016-08-11',
                                              num_pages=100,
                                              book_format=1,
                                              is_ebook=False,
                                              is_original=True,
                                              summary=self.book,
                                              publisher=self.publisher)
        self.book_series = BookSeries.objects.create(book=self.book,
                                                     series=self.series,
                                                     position='1')
        self.book_series.save()
        self.edition_author = EditionAuthor.objects.create(edition=self.edition,
                                                           author=self.author,
                                                           book=self.book,
                                                           role=1)
        self.edition_author.save()

    def test_counts_books(self):
        all_books = Book.objects.all()
        self.assertEqual(len(all_books), 1)

    def test_book_str(self):
        book = Book.objects.get(pk=self.book.pk)
        self.assertEqual(book.__str__(), book.name_eng)

    def test_editions(self):
        book = Book.objects.get(pk=self.book.pk)
        self.assertEqual(book.get_editions()[0], Edition.objects.all()[0])

    def test_authors(self):
        book = Book.objects.get(pk=self.book.pk)
        self.assertEqual(book.get_authors()[0].author, self.author)

    def test_series(self):
        book = Book.objects.get(pk=self.book.pk)
        self.assertEqual(book.get_series()[0].series, self.series)

    def test_lang(self):
        book = Book.objects.get(pk=self.book.pk)
        book.get_editions()
        self.assertEqual(book.get_lang(), ['Abkhazian', ])

    def test_pages_range(self):
        book = Book.objects.get(pk=self.book.pk)
        book.get_editions()
        self.assertEqual(book.get_pages()['min'], 100)
        self.assertEqual(book.get_pages()['max'], 100)


class AuthorTestCase(TestCase):
    def setUp(self):
        self.series = Series.objects.create(goodreads_id=1,
                                            name_ru='Серия',
                                            name_eng='Series',
                                            description_ru='Русское описание',
                                            description_eng='English description')
        self.book = Book.objects.create(work_id=1,
                                        content_rating=1,
                                        plot_structures=1,
                                        time_of_action=1,
                                        name_ru='Название',
                                        name_eng='Title',
                                        description_ru='Русское описание',
                                        description_eng='English description')
        self.author = Author.objects.create(goodreads_id=1,
                                            gender=1,
                                            hometown='City_of_test',
                                            born_at='2016-08-11',
                                            died_at='2016-08-11',
                                            name_ru='Имя',
                                            name_eng='Name',
                                            description_ru='Русское описание',
                                            description_eng='English description')
        self.publisher = Publisher.objects.create(description_ru='Русское описание',
                                                  description_eng='English description',
                                                  name='Test publisher')
        self.edition = Edition.objects.create(goodreads_id=1,
                                              title='Test edition 1',
                                              description='test descr',
                                              language='abk',
                                              isbn='0451524934',
                                              isbn13='9780451524935',
                                              asin='0451524934',
                                              kindle_asin='',
                                              publication_date='2016-08-11',
                                              num_pages=100,
                                              book_format=1,
                                              is_ebook=False,
                                              is_original=True,
                                              summary=self.book,
                                              publisher=self.publisher)
        self.book_series = BookSeries.objects.create(book=self.book,
                                                     series=self.series,
                                                     position='1')
        self.book_series.save()
        self.edition_author = EditionAuthor.objects.create(edition=self.edition,
                                                           author=self.author,
                                                           book=self.book,
                                                           role=1)
        self.edition_author.save()

    def test_count_authors(self):
        all_authors = Author.objects.all()
        self.assertEqual(len(all_authors), 1)

    def test_author_str(self):
        author = Author.objects.get(pk=self.author.pk)
        self.assertEqual(author.__str__(), author.name_eng)


class EditionTestCase(TestCase):
    def setUp(self):
        self.series = Series.objects.create(goodreads_id=1,
                                            name_ru='Серия',
                                            name_eng='Series',
                                            description_ru='Русское описание',
                                            description_eng='English description')
        self.book = Book.objects.create(work_id=1,
                                        content_rating=1,
                                        plot_structures=1,
                                        time_of_action=1,
                                        name_ru='Название',
                                        name_eng='Title',
                                        description_ru='Русское описание',
                                        description_eng='English description')
        self.author = Author.objects.create(goodreads_id=1,
                                            gender=1,
                                            hometown='City_of_test',
                                            born_at='2016-08-11',
                                            died_at='2016-08-11',
                                            name_ru='Имя',
                                            name_eng='Name',
                                            description_ru='Русское описание',
                                            description_eng='English description')
        self.publisher = Publisher.objects.create(description_ru='Русское описание',
                                                  description_eng='English description',
                                                  name='Test publisher')
        self.edition = Edition.objects.create(goodreads_id=1,
                                              title='Test edition 1',
                                              description='test descr',
                                              language='abk',
                                              isbn='0451524934',
                                              isbn13='9780451524935',
                                              asin='0451524934',
                                              kindle_asin='',
                                              publication_date='2016-08-11',
                                              num_pages=100,
                                              book_format=1,
                                              is_ebook=False,
                                              is_original=True,
                                              summary=self.book,
                                              publisher=self.publisher)
        self.book_series = BookSeries.objects.create(book=self.book,
                                                     series=self.series,
                                                     position='1')
        self.book_series.save()
        self.edition_author = EditionAuthor.objects.create(edition=self.edition,
                                                           author=self.author,
                                                           book=self.book,
                                                           role=1)
        self.edition_author.save()

    def test_count_editions(self):
        all_editions = Edition.objects.all()
        self.assertEqual(len(all_editions), 1)

    def test_edition_str(self):
        edition = Edition.objects.get(pk=self.edition.pk)
        self.assertEqual(edition.__str__(), edition.title)

    def test_original_is_set_only_once(self):
        edition = Edition(goodreads_id=2,
                          title='Test edition 2',
                          description='test descr 2',
                          language='abk',
                          isbn='0451524934',
                          publication_date=datetime.date(2016, 8, 9),
                          num_pages=100,
                          book_format=1,
                          is_ebook=False,
                          summary=self.book,
                          publisher=self.publisher)
        self.assertEqual(edition.isbn13, '')
        self.assertFalse(edition.is_original)
        edition.clean()
        self.assertTrue(edition.is_original)
        self.assertEqual(edition.isbn13, '9780451524935')

    # def test_clean(self):
    #     edition = Edition(_width=100)
    #     self.assertRaises(ValidationError, edition.clean)


class PublisherTestCase(TestCase):
    def setUp(self):
        self.series = Series.objects.create(goodreads_id=1,
                                            name_ru='Серия',
                                            name_eng='Series',
                                            description_ru='Русское описание',
                                            description_eng='English description')
        self.book = Book.objects.create(work_id=1,
                                        content_rating=1,
                                        plot_structures=1,
                                        time_of_action=1,
                                        name_ru='Название',
                                        name_eng='Title',
                                        description_ru='Русское описание',
                                        description_eng='English description')
        self.author = Author.objects.create(goodreads_id=1,
                                            gender=1,
                                            hometown='City_of_test',
                                            born_at='2016-08-11',
                                            died_at='2016-08-11',
                                            name_ru='Имя',
                                            name_eng='Name',
                                            description_ru='Русское описание',
                                            description_eng='English description')
        self.publisher = Publisher.objects.create(description_ru='Русское описание',
                                                  description_eng='English description',
                                                  name='Test publisher')
        self.edition = Edition.objects.create(goodreads_id=1,
                                              title='Test edition 1',
                                              description='test descr',
                                              language='abk',
                                              isbn='0451524934',
                                              isbn13='9780451524935',
                                              asin='0451524934',
                                              kindle_asin='',
                                              publication_date='2016-08-11',
                                              num_pages=100,
                                              book_format=1,
                                              is_ebook=False,
                                              is_original=True,
                                              summary=self.book,
                                              publisher=self.publisher)
        self.book_series = BookSeries.objects.create(book=self.book,
                                                     series=self.series,
                                                     position='1')
        self.book_series.save()
        self.edition_author = EditionAuthor.objects.create(edition=self.edition,
                                                           author=self.author,
                                                           book=self.book,
                                                           role=1)
        self.edition_author.save()

    def test_count_publishers(self):
        all_publishers = Edition.objects.all()
        self.assertEqual(len(all_publishers), 1)

    def test_publisher_str(self):
        publisher = Publisher.objects.get(pk=self.publisher.pk)
        self.assertEqual(publisher.__str__(), publisher.name)


class SeriesTestCase(TestCase):
    def setUp(self):
        self.series = Series.objects.create(goodreads_id=1,
                                            name_ru='Серия',
                                            name_eng='Series',
                                            description_ru='Русское описание',
                                            description_eng='English description')
        self.book = Book.objects.create(work_id=1,
                                        content_rating=1,
                                        plot_structures=1,
                                        time_of_action=1,
                                        name_ru='Название',
                                        name_eng='Title',
                                        description_ru='Русское описание',
                                        description_eng='English description')
        self.author = Author.objects.create(goodreads_id=1,
                                            gender=1,
                                            hometown='City_of_test',
                                            born_at='2016-08-11',
                                            died_at='2016-08-11',
                                            name_ru='Имя',
                                            name_eng='Name',
                                            description_ru='Русское описание',
                                            description_eng='English description')
        self.publisher = Publisher.objects.create(description_ru='Русское описание',
                                                  description_eng='English description',
                                                  name='Test publisher')
        self.edition = Edition.objects.create(goodreads_id=1,
                                              title='Test edition 1',
                                              description='test descr',
                                              language='abk',
                                              isbn='0451524934',
                                              isbn13='9780451524935',
                                              asin='0451524934',
                                              kindle_asin='',
                                              publication_date='2016-08-11',
                                              num_pages=100,
                                              book_format=1,
                                              is_ebook=False,
                                              is_original=True,
                                              summary=self.book,
                                              publisher=self.publisher)
        self.book_series = BookSeries.objects.create(book=self.book,
                                                     series=self.series,
                                                     position='1')
        self.book_series.save()
        self.edition_author = EditionAuthor.objects.create(edition=self.edition,
                                                           author=self.author,
                                                           book=self.book,
                                                           role=1)
        self.edition_author.save()

    def test_count_series(self):
        all_series = Edition.objects.all()
        self.assertEqual(len(all_series), 1)

    def test_edition_str(self):
        series = Series.objects.get(pk=self.series.pk)
        self.assertEqual(series.__str__(), series.name_eng)
