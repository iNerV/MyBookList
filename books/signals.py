from django.dispatch import receiver
from django.db import models
from django.utils.translation import ugettext_lazy as _

import os
import shutil

from books.models import Edition, AuthorPhoto, CoverOfPublisher, Publisher


@receiver(models.signals.post_delete, sender=Edition)
@receiver(models.signals.post_delete, sender=AuthorPhoto)
@receiver(models.signals.post_delete, sender=CoverOfPublisher)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
    if instance.image_xs:
        if os.path.isfile(instance.image_xs.path):
            os.remove(instance.image_xs.path)
    if instance.image_sm:
        if os.path.isfile(instance.image_sm.path):
            os.remove(instance.image_sm.path)
    if instance.image_md:
        if os.path.isfile(instance.image_md.path):
            os.remove(instance.image_md.path)


@receiver(models.signals.pre_save, sender=Edition)
@receiver(models.signals.pre_save, sender=AuthorPhoto)
@receiver(models.signals.pre_save, sender=CoverOfPublisher)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return False

    old_image = obj.image
    old_image_xs = obj.image_xs
    old_image_sm = obj.image_sm
    old_image_md = obj.image_md

    if not old_image or not old_image_md or not old_image_sm or not old_image_xs:
        print('Bleat')
        return False

    new_file = instance.image
    if not old_image == new_file:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
        if os.path.isfile(old_image_xs.path):
            instance.image_xs = ''
            os.remove(old_image_xs.path)
        if os.path.isfile(old_image_sm.path):
            os.remove(old_image_sm.path)
            instance.image_sm = ''
        if os.path.isfile(old_image_md.path):
            os.remove(old_image_md.path)
            instance.image_md = ''


@receiver(models.signals.pre_delete, sender=Publisher)
def auto_delete_file(sender, instance, **kwargs):
    cover = CoverOfPublisher.objects.filter(publisher=instance).all()
    for c in cover:
        if c.image:
            shutil.rmtree(os.path.dirname(c.image.path), ignore_errors=True)


@receiver(models.signals.post_save, sender=Edition)
@receiver(models.signals.post_save, sender=AuthorPhoto)
@receiver(models.signals.post_save, sender=CoverOfPublisher)
def make_thumb(sender, instance, **kwargs):
    if not instance.image_xs and instance.image:
        if not instance.make_thumbnail('xs'):
            raise Exception(_('Could not create thumbnail - is the file type valid?'))
    if not instance.image_sm and instance.image:
        if not instance.make_thumbnail('sm'):
            raise Exception(_('Could not create thumbnail - is the file type valid?'))
    if not instance.image_md and instance.image:
        if not instance.make_thumbnail('md'):
            raise Exception(_('Could not create thumbnail - is the file type valid?'))
