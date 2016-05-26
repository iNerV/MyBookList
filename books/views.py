from django.views.generic import ListView, DetailView
from django.db.models import Max, Min
from books.models import BookSummary, Author, Series


class BooksList(ListView):
    model = BookSummary
    template_name = 'books/books_list.html'
    paginate_by = 50

    # def get_context_data(self, **kwargs):
    #     context = super(BooksList, self).get_context_data(**kwargs)


class BooksSummary(DetailView):
    model = BookSummary
    template_name = 'books/books_summary.html'

    def get_context_data(self, **kwargs):
        context = super(BooksSummary, self).get_context_data(**kwargs)
        bs = self.object
        books = bs.book_set.all()
        authors = bs.bookauthor_set.all()\
            .select_related('author',
                            'book',
                            'booksummary')\
            .order_by('author')\
            .distinct('author')
        series = bs.bookseries_set.all()\
            .select_related('series',
                            'book',
                            'booksummary')\
            .order_by('series')\
            .distinct('series')
        lang = set([x.get_language_display() for x in books])
        book_format = set([x.get_book_format_display() for x in books])
        prim_cover = None
        for x in books:
            if x.is_original:
                prim_cover = x.cover.url
        context['books'] = books
        context['num_pages'] = books.distinct().aggregate(min=Min('num_pages'), max=Max('num_pages'))
        context['lang'] = list(lang)[:2]
        context['format'] = list(book_format)[:2]
        context['authors'] = authors
        context['series'] = series
        context['cover'] = prim_cover
        # context['req'] = self.request.user.is_authenticated()  # на будущее
        return context


class SeriesDetail(DetailView):
    model = Series
    template_name = 'books/series_detail.html'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'books/author_detail.html'


class AuthorsList(DetailView):
    model = Author
    template_name = 'books/authors_list.html'
