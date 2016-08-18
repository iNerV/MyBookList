from django.conf.urls import url

from books.views import *

urlpatterns = [
    url(r'^$', AuthorsList.as_view(), name='authors-list'),
    url(r'^(?P<pk>\d+)/$', AuthorDetail.as_view(), name='author-detail'),
]
