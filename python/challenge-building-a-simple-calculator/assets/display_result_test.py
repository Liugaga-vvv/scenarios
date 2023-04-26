import sys

sys.path.append("/home/labex/project")
import unittest
from io import StringIO
from unittest.mock import patch
from simple_calculator import simple_calculator


class TestStep4(unittest.TestCase):
    def test_display_result(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            simple_calculator().display_result(15.0)
        self.assertEqual(fake_out.getvalue().strip(), "Result: 15.0")


if __name__ == "__main__":
    unittest.main()
