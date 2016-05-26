from django.contrib import admin
from books.models import BookSummary,\
    Author,\
    Series,\
    Book,\
    Publisher,\
    CoverOfPublisher,\
    BookAuthor,\
    BookSeries,\
    BookGenres,\
    AuthorPhoto


class BookInline(admin.TabularInline):
    model = Book
    extra = 1


class PhotoOfAuthorInline(admin.TabularInline):
    model = AuthorPhoto
    extra = 1


class CoverOfPublisherInline(admin.TabularInline):
    model = CoverOfPublisher
    extra = 1


class AuthorInline(admin.TabularInline):
    model = BookAuthor
    extra = 1


class SeriesInline(admin.TabularInline):
    model = BookSeries
    extra = 1


class GenresInline(admin.TabularInline):
    model = BookGenres
    extra = 1


class PublisherAdmin(admin.ModelAdmin):
    inlines = [CoverOfPublisherInline]


class BookAdmin(admin.ModelAdmin):
    inlines = [AuthorInline, SeriesInline]


class AuthorAdmin(admin.ModelAdmin):
    inlines = [PhotoOfAuthorInline]


class SummaryAdmin(admin.ModelAdmin):
    inlines = [GenresInline]


admin.site.register(BookSummary, SummaryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Series)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
