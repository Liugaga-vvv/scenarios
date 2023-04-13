import unittest
import sys

sys.path.append("/home/labex/project")
from check_age_limit import check_age_limit

class TestCheckAgeLimit(unittest.TestCase):
    """Tests for the check_age_limit function"""

    def test_age_above_18(self):
        """Should return True for ages above 18"""
        self.assertTrue(check_age_limit(22))

    def test_age_below_18(self):
        """Should return False for ages below 18"""
        self.assertFalse(check_age_limit(16))

    def test_age_equal_to_18(self):
        """Should return True for age equal to 18"""
        self.assertTrue(check_age_limit(18))

if __name__ == '__main__':
    unittest.main()