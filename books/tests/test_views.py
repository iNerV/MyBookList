from django.test import TestCase
from django.test import Client

from books.models import *


class TestBook(TestCase):

    def setUp(self):
        self.client = Client()
        self.series = Series.objects.create(goodreads_id=1,
                                            name_ru='Серия',
                                            name_eng='Series',
                                            description_ru='Русское описание серии',
                                            description_eng='English description of series')
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
                                            died_at='2016-08-12',
                                            name_ru='Имя автора',
                                            name_eng='Name author',
                                            description_ru='Русское описание автора',
                                            description_eng='English description of author')
        self.publisher = Publisher.objects.create(description_ru='Русское описание',
                                                  description_eng='English description',
                                                  name='Test publisher')
        self.edition = Edition.objects.create(goodreads_id=1,
                                              title='Test edition 1',
                                              description='test descr',
                                              language='abk',
                                              isbn='0451524934',
                                              isbn13='9780451524935',
                                              asin='ASIN',
                                              kindle_asin='kASIN',
                                              publication_date='2016-08-11',
                                              num_pages=100,
                                              book_format=1,
                                              is_ebook=False,
                                              is_original=True,
                                              summary=self.book,
                                              publisher=self.publisher)
        self.book_series = BookSeries.objects.create(book=self.book,
                                                     series=self.series,
                                                     position='123')
        self.book_series.save()
        self.edition_author = EditionAuthor.objects.create(edition=self.edition,
                                                           author=self.author,
                                                           book=self.book,
                                                           role=1)
        self.edition_author.save()

    def test_access(self):
        book = self.book.id
        response = self.client.get(reverse('book-summary', args=(book,)))
        self.assertEqual(response.status_code, 200)

    def test_get_absolute_url(self):
        book = self.book
        self.assertIsNotNone(book.get_absolute_url())

    def test_titles(self):
        book = self.book.id
        response = self.client.get(reverse('book-summary', args=(book,)))
        self.assertContains(response, 'Title')
        self.assertContains(response, 'Название')

    def test_descrs(self):
        book = self.book.id
        response = self.client.get(reverse('book-summary', args=(book,)))
        self.assertContains(response, 'Русское описание')
        self.assertContains(response, 'English description')

    def test_isbns(self):
        book = self.book.id
        response = self.client.get(reverse('book-summary', args=(book,)))
        self.assertContains(response, '0451524934')
        self.assertContains(response, '9780451524935')
        self.assertContains(response, 'kASIN')
        self.assertContains(response, 'ASIN')

    def test_dirs_pub_date(self):
        book = self.book.id
        response = self.client.get(reverse('book-summary', args=(book,)))
        # self.assertContains(response, '11/08/2016')  # fixme

    def test_numbers_of_pages(self):
        book = self.book.id
        response = self.client.get(reverse('book-summary', args=(book,)))
        self.assertContains(response, 100)  # количество страниц

    def test_position_in_series(self):
        book = self.book.id
        response = self.client.get(reverse('book-summary', args=(book,)))
        self.assertContains(response, '123')  # номер в серии

    def test_plot_structure(self):
        book = self.book.id
        response = self.client.get(reverse('book-summary', args=(book,)))
        self.assertContains(response, 'Линейный')

    def test_time_of_action(self):
        book = self.book.id
        response = self.client.get(reverse('book-summary', args=(book,)))
        self.assertContains(response, 'Дочеловеческие времена')

    def test_age_rating(self):
        book = self.book.id
        response = self.client.get(reverse('book-summary', args=(book,)))
        self.assertContains(response, 'Для детей.')

    def test_langs(self):
        book = self.book.id
        response = self.client.get(reverse('book-summary', args=(book,)))
        self.assertContains(response, 'Abkhazian')

    def test_types(self):
        book = self.book.id
        response = self.client.get(reverse('book-summary', args=(book,)))
        self.assertContains(response, 'Hardcover')

    def test_series(self):
        book = self.book.id
        response = self.client.get(reverse('book-summary', args=(book,)))
        self.assertContains(response, 'Серия')  # fixme
        self.assertContains(response, 'Series')  # fixme

    def test_authors(self):
        book = self.book.id
        response = self.client.get(reverse('book-summary', args=(book,)))
        self.assertContains(response, 'Имя автора')  # fixme
        self.assertContains(response, 'Name author')  # fixme


class TestAuthor(TestCase):

    def setUp(self):
        self.client = Client()
        self.series = Series.objects.create(goodreads_id=1,
                                            name_ru='Серия',
                                            name_eng='Series',
                                            description_ru='Русское описание серии',
                                            description_eng='English description of series')
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
                                            died_at='2016-08-12',
                                            name_ru='Имя автора',
                                            name_eng='Name author',
                                            description_ru='Русское описание автора',
                                            description_eng='English description of author')
        self.publisher = Publisher.objects.create(description_ru='Русское описание',
                                                  description_eng='English description',
                                                  name='Test publisher')
        self.edition = Edition.objects.create(goodreads_id=1,
                                              title='Test edition 1',
                                              description='test descr',
                                              language='abk',
                                              isbn='0451524934',
                                              isbn13='9780451524935',
                                              asin='ASIN',
                                              kindle_asin='kASIN',
                                              publication_date='2016-08-11',
                                              num_pages=100,
                                              book_format=1,
                                              is_ebook=False,
                                              is_original=True,
                                              summary=self.book,
                                              publisher=self.publisher)
        self.book_series = BookSeries.objects.create(book=self.book,
                                                     series=self.series,
                                                     position='123')
        self.book_series.save()
        self.edition_author = EditionAuthor.objects.create(edition=self.edition,
                                                           author=self.author,
                                                           book=self.book,
                                                           role=1)
        self.edition_author.save()

    def test_access(self):
        author = self.author.id
        response = self.client.get(reverse('author-detail', args=(author,)))
        self.assertEqual(response.status_code, 200)

    def test_names(self):
        author = self.author.id
        response = self.client.get(reverse('author-detail', args=(author,)))
        self.assertContains(response, 'Name author')
        self.assertContains(response, 'Имя автора')

    def test_descrs(self):
        author = self.author.id
        response = self.client.get(reverse('author-detail', args=(author,)))
        self.assertContains(response, 'Русское описание автора')
        self.assertContains(response, 'English description of author')

    def test_dates(self):
        author = self.author.id
        response = self.client.get(reverse('author-detail', args=(author,)))
        self.assertContains(response, '11/08/2016')
        self.assertContains(response, '12/08/2016')

    def test_city(self):
        author = self.author.id
        response = self.client.get(reverse('author-detail', args=(author,)))
        self.assertContains(response, 'City_of_test')

    def test_gender(self):
        author = self.author.id
        response = self.client.get(reverse('author-detail', args=(author,)))
        self.assertContains(response, 'Мужчина')


class TestSeries(TestCase):

    def setUp(self):
        self.client = Client()
        self.series = Series.objects.create(goodreads_id=1,
                                            name_ru='Серия',
                                            name_eng='Series',
                                            description_ru='Русское описание серии',
                                            description_eng='English description of series')
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
                                            died_at='2016-08-12',
                                            name_ru='Имя автора',
                                            name_eng='Name author',
                                            description_ru='Русское описание автора',
                                            description_eng='English description of author')
        self.publisher = Publisher.objects.create(description_ru='Русское описание',
                                                  description_eng='English description',
                                                  name='Test publisher')
        self.edition = Edition.objects.create(goodreads_id=1,
                                              title='Test edition 1',
                                              description='test descr',
                                              language='abk',
                                              isbn='0451524934',
                                              isbn13='9780451524935',
                                              asin='ASIN',
                                              kindle_asin='kASIN',
                                              publication_date='2016-08-11',
                                              num_pages=100,
                                              book_format=1,
                                              is_ebook=False,
                                              is_original=True,
                                              summary=self.book,
                                              publisher=self.publisher)
        self.book_series = BookSeries.objects.create(book=self.book,
                                                     series=self.series,
                                                     position='123')
        self.book_series.save()
        self.edition_author = EditionAuthor.objects.create(edition=self.edition,
                                                           author=self.author,
                                                           book=self.book,
                                                           role=1)
        self.edition_author.save()

    def test_access(self):
        series = self.series.id
        response = self.client.get(reverse('series-detail', args=(series,)))
        self.assertEqual(response.status_code, 200)

    def test_titles(self):
        series = self.series.id
        response = self.client.get(reverse('series-detail', args=(series,)))
        self.assertContains(response, 'Series')
        self.assertContains(response, 'Серия')

    def test_descrs(self):
        series = self.series.id
        response = self.client.get(reverse('series-detail', args=(series,)))
        self.assertContains(response, 'Русское описание серии')
        self.assertContains(response, 'English description of series')
