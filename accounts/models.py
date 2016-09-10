from django.db import models
# from django.contrib.auth import password_validation
import hashlib
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.postgres.fields import JSONField
from autoslug import AutoSlugField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from precise_bbcode.fields import BBCodeTextField

from core.constants import *
from books.models import Book


class User(AbstractUser):  # FIXME валидатор пофиксить, не те символы допускает
    slug = AutoSlugField(populate_from='username', unique=True, always_update=True)
    gender = models.IntegerField(choices=GENDER, default=0)
    city = models.CharField(max_length=200, blank=True)
    born_at = models.DateField(null=True, blank=True)
    about = BBCodeTextField(blank=True)
    # preference = models.CharField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def avatar(self):
        return 'http://www.gravatar.com/avatar/%s.jpg?s=200&d=wavatar' % self.get_md5()

    def get_md5(self):
        m = hashlib.md5()
        m.update(self.email.encode('utf8'))
        return m.hexdigest()

    def get_email(self):
        return self.email

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'slug': self.slug})


class DataChanges(models.Model):
    user = models.ForeignKey(User)
    object_id = models.PositiveIntegerField()  # - id изменяемой сущности
    content_type = models.ForeignKey(ContentType)
    content_object = GenericForeignKey('content_type', 'object_id')
    data = JSONField()  # - сериализованный массив с измененяющимеся полями
    state = models.IntegerField(choices=STATE, default=0)  # - статус правки
    approver_id = models.ForeignKey(User, editable=False)  # - ид принявшего/отказавшего/удалившего правку
    created_at = models.DateTimeField(auto_now_add=True, editable=False)  # - дата создания


class BookList(models.Model):
    user = models.ForeignKey(User)
    book = models.ManyToManyField(Book)
    list = models.IntegerField(choices=LISTS)

    class Meta:
        verbose_name = _('Список книг')
        verbose_name_plural = _('Списки книг')
        unique_together = ('user', 'list')

    def __str__(self):
        return self.get_list_display()


User._meta.get_field('email')._unique = True  # MAGIC!
User._meta.get_field('email')._blank = False  # MAGIC!
