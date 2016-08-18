from django.test import TestCase

from books.utils import *


class TestISBN(TestCase):
    # def test_isbn_converter(self):
    #     self.assertEqual(check_digit_10('045152493'), '4')
    #     self.assertEqual(check_digit_13('978045152493'), '5')

    def test_isbn_converter(self):
        self.assertEqual(check_digit_10('045152493'), '4')
        self.assertEqual(check_digit_13('978045152493'), '5')
        self.assertEqual(convert_10_to_13('0451524934'), '9780451524935')
