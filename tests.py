import datetime
import unittest

from holidays import is_holiday


class Test(unittest.TestCase):
    def test_is_holiday(self):
        self.assertTrue(is_holiday(datetime.date(2012, 3, 8)))
        self.assertTrue(is_holiday(datetime.date(2012, 3, 31)))
        self.assertFalse(is_holiday(datetime.date(2012, 3, 11)))
        self.assertFalse(is_holiday(datetime.date(2012, 9, 3)))

    def test_bad_date(self):
        self.assertRaises(ValueError, is_holiday, datetime.date(2000, 1, 1))
        self.assertRaises(ValueError, is_holiday, datetime.date(2432, 1, 1))

if __name__ == '__main__':
    unittest.main()
