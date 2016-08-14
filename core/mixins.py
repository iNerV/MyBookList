from io import BytesIO
from PIL import Image
import os

from mbl.settings import THUMB_SIZE

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage

from core.models import ImageField
from core.utils import image_to


class AbstractBilingual(models.Model):
    class Meta:
        abstract = True

    name_ru = models.CharField(max_length=400, blank=True)
    name_eng = models.CharField(max_length=400, blank=True)
    description_ru = models.TextField(blank=True)
    description_eng = models.TextField(blank=True)

    def clean(self):
        if self.name_eng == '' and self.name_ru is '':
            raise ValidationError({
                'name_ru': ValidationError(_('Поле обязательно для заполнения.'), code='required'),
                'name_eng': ValidationError(_('Поле обязательно для заполнения.'), code='required'),
            })


class AbstractImage(models.Model):
    class Meta:
        abstract = True

    image = ImageField(upload_to=image_to, blank=True, width_field='_width')  # original
    image_xs = ImageField(upload_to=image_to, blank=True, image_size_type='xs', editable=False)  # 48
    image_sm = ImageField(upload_to=image_to, blank=True, image_size_type='sm', editable=False)  # 96
    image_md = ImageField(upload_to=image_to, blank=True, image_size_type='md', editable=False)  # 120

    _width = int()

    def clean(self):
        if self._width < THUMB_SIZE['md']:
            raise ValidationError(_('Минимальная ширина изображения {}px'.format(THUMB_SIZE['md'])))

    def save(self, *args, **kwargs):
        super(AbstractImage, self).save(*args, **kwargs)
        if not self.image_xs and self.image:
            if not self.make_thumbnail('xs'):
                raise Exception('Could not create thumbnail - is the file type valid?')
        if not self.image_sm and self.image:
            if not self.make_thumbnail('sm'):
                raise Exception('Could not create thumbnail - is the file type valid?')
        if not self.image_md and self.image:
            if not self.make_thumbnail('md'):
                raise Exception('Could not create thumbnail - is the file type valid?')

    def make_thumbnail(self, size):
        """
        Create and save the thumbnail for the photo (simple resize with PIL).
        """
        fh = storage.open(self.image.name, 'rb')
        try:
            image = Image.open(fh)
        except IOError:
            return False

        basewidth = THUMB_SIZE[str(size)]  # notice Ширина
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image.thumbnail((basewidth, hsize), Image.LANCZOS)
        fh.close()

        # Path to save to, name, and extension
        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_extension = thumb_extension.lower()

        thumb_name = thumb_name.split('/')[-1]

        thumb_filename = thumb_name + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            ftype = 'JPEG'
        elif thumb_extension == '.gif':
            ftype = 'GIF'
        elif thumb_extension == '.png':
            ftype = 'PNG'
        else:
            return False  # Unrecognized file type

        # Save thumbnail to in-memory file as BytesIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, ftype)
        temp_thumb.seek(0)

        image = ''
        if size == 'xs':
            image = self.image_xs
        elif size == 'sm':
            image = self.image_sm
        elif size == 'md':
            image = self.image_md

        # Load a ContentFile into the thumbnail field so it gets saved
        image.save(thumb_filename, ContentFile(temp_thumb.read()), save=True)
        temp_thumb.close()

        return True
