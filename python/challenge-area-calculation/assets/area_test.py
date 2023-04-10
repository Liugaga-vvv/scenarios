import sys
from unittest.mock import patch

sys.path.append("/home/labex/project")
from area import cal_area

import unittest


class TestSubclass(unittest.TestCase):
    @patch("builtins.input", side_effect=["1 10"])
    def test_circle(self, input_str):
        shape, area = cal_area()
        self.assertEqual("circle", shape)
        self.assertTrue(abs(area - 3.14 * 10 * 10) < 0.1)

    @patch("builtins.input", side_effect=["2 10"])
    def test_sqaure(self, input_str):
        shape, area = cal_area()
        self.assertEqual("square", shape)
        self.assertEqual(100, area)


if __name__ == "__main__":
    unittest.main()
