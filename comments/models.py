from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import User
from precise_bbcode.fields import BBCodeTextField


class Comments(models.Model):
    COMMENT_TYPES = (
        (0, _('Комментарий')),
        (1, _('Оффтоп')),
        (2, _('Отзыв'))

    )

    user = models.ForeignKey(User)
    parent_id = models.ForeignKey('self', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    text = BBCodeTextField()
    comment_type = models.IntegerField(choices=COMMENT_TYPES, default=0)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    content_object = GenericForeignKey('content_type', 'object_id')
