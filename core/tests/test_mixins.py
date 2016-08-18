from django.test import TestCase

from core.mixins import *

from mbl.settings import THUMB_SIZE


class BilingualTestCase(TestCase):

    def test_clean(self):
        ab = AbstractBilingual()
        self.assertRaises(ValidationError, ab.clean)


class ImageTestCase(TestCase):

    def test_clean_with_small_img(self):
        ai = AbstractImage()
        ai._width = THUMB_SIZE['md'] - 1
        self.assertRaises(ValidationError, ai.clean)
