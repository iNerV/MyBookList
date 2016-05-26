from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.UsersList.as_view(), name='user-list'),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/edit$', views.UserSettings.as_view(), name='user-settings'),
]
