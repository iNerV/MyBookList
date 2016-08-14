import os
import sys
import django
from grab import Grab
import re
import logging
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYS_PATH = os.path.dirname(BASE_DIR)
if SYS_PATH not in sys.path:
    sys.path.append(SYS_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mbl.settings'
django.setup()

from django.conf import settings
from books.models import Edition, Author, Series, EditionAuthor, Book, BookSeries, Publisher

logger = logging.getLogger('grab')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

# http://ec2.images-amazon.com/images/P/0553801473.00._PE20_SCLZZZZZZZ_.png


def save_image(img, instance, instance_id):
    if 'nophoto' in img:
        print('NOPHOTO!')
    else:
        img = re.sub(r'(/[0-9]+)(m/)', r'\1l/', img)
        p = requests.get(img)
        cover_name = img.split('/')[5]
        out = open(settings.MEDIA_ROOT + instance + instance_id + cover_name, "wb")
        out.write(p.content)
        out.close()
        return settings.MEDIA_ROOT + instance + instance_id + cover_name


def gr_parser(gr_id,):
    g = Grab()
    g.go('https://www.goodreads.com/book/show/' + str(gr_id) + '?format=xml&key=7TJ8xCWO2bcwRid2t1UxvQ',
         content_type='xml',
         follow_location=False)

    if g.response.code != 200:
        pass
    else:
        goodreads_id = g.doc.select('//id').text()
        title = g.doc.select('//title').text()
        description = re.sub(r'<[^>]*>', '', g.doc.select('//description').text())
        language = g.doc.select('//language_code').text()
        cover = g.doc.select('//image_url').text()
        isbn = g.doc.select('//isbn').text()
        isbn13 = g.doc.select('//isbn13').text()
        asin = g.doc.select('//asin').text()
        kindle_asin = g.doc.select('//kindle_asin').text()

        publication_year = g.doc.select('//publication_year').text()
        publication_month = g.doc.select('//publication_month').text()
        publication_day = g.doc.select('//publication_day').text()
        publication_date = publication_year + '-' + publication_month + '-' + publication_day

        num_pages = g.doc.select('//num_pages').text()
        book_format = g.doc.select('//format').text()
        is_ebook = g.doc.select('//is_ebook').text()

        publisher = g.doc.select('//publisher').text()

        authors = g.doc.select('/GoodreadsResponse/book/authors/author')
        author = []
        for x in authors:
            author.append({'id': x.select('id').text(),
                           'name': x.select('name').text(),
                           'role': x.select('role').text(),
                           'image': x.select('image_url').text()})  # TODO сделать сохранение картинки на сервер

        all_series = g.doc.select('//series_works/series_work')
        series = []
        for x in all_series:
            series.append({'id': x.select('series/id').text(),
                           'title': x.select('series/title').text(),
                           'description': re.sub(r'<[^>]*>', '', x.select('series/description').text())})

        position_in_series = g.doc.select('//series_works/series_work/user_position').text()
        work_id = g.doc.select('//work//id').text()
        original_title = g.doc.select('//original_title').text()
        original_publication_year = g.doc.select('//original_publication_year').text()
        original_publication_month = g.doc.select('//original_publication_month').text()
        original_publication_day = g.doc.select('//original_publication_day').text()
        original_publication_date = original_publication_year + \
                                    '-' + \
                                    original_publication_month + \
                                    '-' + \
                                    original_publication_day

        print(goodreads_id,
              title, description, language, cover, isbn, isbn13, asin, kindle_asin,
              '-----',
              publication_date, num_pages, book_format, is_ebook, publisher,
              '-----',
              author,
              '-----',
              series,
              '-----',
              work_id, original_title,
              original_publication_date, sep='\n')

        if book_format == 'Hardcover':
            book_format = 1
        elif book_format == 'Paperback':
            book_format = 2
        elif book_format == 'Kindle Edition':
            book_format = 3
        elif book_format == 'ebook':
            book_format = 4
        elif book_format == 'Mass Market Paperback':
            book_format = 5
        elif book_format == 'Nook':
            book_format = 6
        elif book_format == 'Library Binding':
            book_format = 7
        elif book_format == 'Audiobook':
            book_format = 8
        elif book_format == 'Audio CD':
            book_format = 9
        elif book_format == 'Audio Cassette':
            book_format = 10
        elif book_format == 'Audible Audio':
            book_format = 11
        elif book_format == 'CD-ROM':
            book_format = 12
        elif book_format == 'MP3 CD':
            book_format = 13
        elif book_format == 'Board book':
            book_format = 14
        elif book_format == 'Leather Bound':
            book_format = 15
        elif book_format == 'Unbound':
            book_format = 16
        elif book_format == 'Spiral-bound':
            book_format = 17
        else:
            book_format = 0

        new_publisher, created = Publisher.objects.get_or_create(name=publisher)

        book_sum, created = Book.objects.get_or_create(work_id=work_id,
                                                       original_title=original_title,
                                                       original_publication_date=original_publication_date)

        new_book, created = Edition.objects.get_or_create(goodreads_id=goodreads_id,
                                                          title=title,
                                                          description=description,
                                                          language=language,
                                                          cover=save_image(cover, 'books/', book_sum),
                                                          isbn=isbn,
                                                          isbn13=isbn13,
                                                          asin=asin,
                                                          kindle_asin=kindle_asin,
                                                          publication_date=publication_date,
                                                          num_pages=num_pages,
                                                          book_format=book_format,
                                                          is_ebook=is_ebook,
                                                          summary=book_sum,
                                                          publisher=new_publisher)

        for val in author:
            new_author, created = Author.objects.get_or_create(goodreads_id=val['id'],
                                                               name=val['name'],
                                                               photo=save_image(val['image'], 'authors/', book_sum))  # FIXME передать id автора - хз как
            book_author = EditionAuthor.objects.create(book=new_book,
                                                       author=new_author,
                                                       role=val['role'])
            book_author.save()

        for val in series:
            new_series, created = Series.objects.get_or_create(goodreads_id=val['id'],
                                                               title=val['title'],
                                                               description=val['description'])
            book_series = BookSeries.objects.create(book=new_book,
                                                    series=new_series,
                                                    position=position_in_series)
            book_series.save()

gr_parser(1)
