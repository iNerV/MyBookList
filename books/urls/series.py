from django.conf.urls import url

from books import views

urlpatterns = [
    url(r'^$', views.BooksList.as_view(), name='books-list'),
    url(r'^(?P<pk>\d+)/$', views.SeriesDetail.as_view(), name='series-detail'),
]
