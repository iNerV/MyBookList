from django.conf.urls import url

from books import views

urlpatterns = [
    url(r'^$', views.AuthorsList.as_view(), name='authors-list'),
    url(r'^(?P<pk>\d+)/$', views.AuthorDetail.as_view(), name='author-detail'),
]
