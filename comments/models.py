from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from core.constants import *
from accounts.models import User
from precise_bbcode.fields import BBCodeTextField


class Comments(models.Model):
    user = models.ForeignKey(User)
    parent_id = models.ForeignKey('self', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    text = BBCodeTextField()
    comment_type = models.IntegerField(choices=COMMENT_TYPES, default=0)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    content_object = GenericForeignKey('content_type', 'object_id')
