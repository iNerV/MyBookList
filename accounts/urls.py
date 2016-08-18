from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', UsersList.as_view(), name='user-list'),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/edit$', UserSettings.as_view(), name='user-settings'),
]
