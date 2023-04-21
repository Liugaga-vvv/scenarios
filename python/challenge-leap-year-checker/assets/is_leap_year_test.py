import sys

sys.path.append("/home/labex/project")

import unittest
from is_leap_year import is_leap_year


class TestIsLeapYear(unittest.TestCase):
    def test_is_leap_year(self):
        self.assertEqual(is_leap_year(2020), True)
        self.assertEqual(is_leap_year(2100), False)
        self.assertEqual(is_leap_year(2000), True)
        self.assertEqual(is_leap_year(1987), False)


if __name__ == "__main__":
    unittest.main()
