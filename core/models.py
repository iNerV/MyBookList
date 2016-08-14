import os

from django.db import models


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
