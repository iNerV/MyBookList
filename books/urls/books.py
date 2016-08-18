from django.conf.urls import url

from books.views import *

urlpatterns = [
    url(r'^$', BooksList.as_view(), name='books-list'),
    url(r'^(?P<pk>\d+)/$', BookDetail.as_view(), name='book-summary'),
]
