from django.dispatch import receiver
from django.db import models

import os

from books.models import Edition, AuthorPhoto


@receiver(models.signals.post_delete, sender=Edition)  # todo проверить
# @receiver(models.signals.pre_save, sender=AuthorPhoto)  # fixme не работает ;(
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
        if os.path.isfile(instance.image_xs.path):
            os.remove(instance.image_xs.path)
        if os.path.isfile(instance.image_sm.path):
            os.remove(instance.image_sm.path)
        if os.path.isfile(instance.image_md.path):
            os.remove(instance.image_md.path)


@receiver(models.signals.pre_save, sender=Edition)
@receiver(models.signals.pre_save, sender=AuthorPhoto)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is changed.
    """
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

    if not old_image:
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
