from io import BytesIO
from PIL import Image
import os

from mbl.settings import THUMB_SIZE

from django.db import models
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage


class ImageField(models.ImageField):
    def __init__(self, image_size_type='', **kwargs):
        self.image_size_type = image_size_type
        super(ImageField, self).__init__(**kwargs)

    def generate_filename(self, instance, filename):
        if callable(self.upload_to):
            directory_name, filename = os.path.split(self.upload_to(instance, filename, self.image_size_type))
            filename = self.storage.get_valid_name(filename)
            return os.path.normpath(os.path.join(directory_name, filename))

        return os.path.join(self.get_directory_name(), self.get_filename(filename))


def image_to(instance, filename, image_size_type):
    folder = instance.__class__.__name__
    if instance.__class__.__name__ == 'Edition':
        folder = 'books'
        instance.fk = instance.summary_id
    elif instance.__class__.__name__ == 'AuthorPhoto':
        folder = 'authors'
        instance.fk = instance.author_id
    elif instance.__class__.__name__ == 'CoverOfPublisher':
        folder = 'publishers'
        instance.fk = instance.publisher_id

    if image_size_type:
        size = '/{}'.format(image_size_type)
    else:
        size = ''
    return '{0}/{1}{2}/{3}'.format(folder.lower(), instance.fk, size, filename)


class AbstractImage(models.Model):
    class Meta:
        abstract = True

    image = ImageField(upload_to=image_to, blank=True)  # original
    image_xs = ImageField(upload_to=image_to, blank=True, image_size_type='xs', editable=False)  # 48
    image_sm = ImageField(upload_to=image_to, blank=True, image_size_type='sm', editable=False)  # 96
    image_md = ImageField(upload_to=image_to, blank=True, image_size_type='md', editable=False)  # 120

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
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False  # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
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
