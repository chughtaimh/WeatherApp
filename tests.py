import unittest

from main import get_html_for_zip, parse_html
from main import location_from_soup, temp_from_soup, cond_from_soup, humidity_from_soup
from utils import remove_tabs_new_lines, validate_zipcode


class AppTests(unittest.TestCase):

    def remove_tablines_test(self):
        self.assertEqual(remove_tabs_new_lines('\nfoo'), 'foo')
        self.assertEqual(remove_tabs_new_lines('\n\tfoo'), 'foo')
        self.assertEqual(remove_tabs_new_lines('foo \t\n\n\n\t'), 'foo ')
        self.assertEqual(remove_tabs_new_lines('\n\n\n\n\nfoo'), 'foo')
        self.assertEqual(remove_tabs_new_lines('\n'), '')
        self.assertEqual(remove_tabs_new_lines('foo'), 'foo')

    def validate_zip_dec(self):
        func = lambda x: x
        # No errors should be raised for 5-digit numeric inputs
        self.assertEqual(validate_zipcode(func)('22213'), '22213')
        self.assertEqual(validate_zipcode(func)('00000'), '00000')
        self.assertEqual(validate_zipcode(func)('10301'), '10301')

        # ValueError should be raised for <> 5-character inputs
        with self.assertRaises(ValueError):
            validate_zipcode(func)('213')
        with self.assertRaises(ValueError):
            validate_zipcode(func)('222213')
        with self.assertRaises(ValueError):
            validate_zipcode(func)('0')
        with self.assertRaises(ValueError):
            validate_zipcode(func)('999999999999999')

        # ValueError should be raised for non-numeric inputs
        with self.assertRaises(ValueError):
            validate_zipcode(func)('foo')
        with self.assertRaises(ValueError):
            validate_zipcode(func)('')
        with self.assertRaises(ValueError):
            validate_zipcode(func)('/')
        with self.assertRaises(ValueError):
            validate_zipcode(func)('.<>}{')


if __name__ == '__main__':
    tests = AppTests()
    tests.remove_tablines_test()
    tests.validate_zip_dec()
