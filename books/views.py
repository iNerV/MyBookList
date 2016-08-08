from django.views.generic import ListView, DetailView
from books.models import Book, Author, Series


class BooksList(ListView):
    model = Book
    template_name = 'books/books_list.html'
    paginate_by = 50


class BookDetail(DetailView):
    model = Book
    template_name = 'books/books_summary.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetail, self).get_context_data(**kwargs)
        context['editions'] = Book.get_editions(self.object)
        context['num_pages'] = Book.get_pages(self.object)
        context['lang'] = Book.get_lang(self.object)
        context['format'] = Book.get_format(self.object)
        context['authors'] = Book.get_authors(self.object)
        context['series'] = Book.get_series(self.object)
        context['cover'] = Book.get_cover(self.object)
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
