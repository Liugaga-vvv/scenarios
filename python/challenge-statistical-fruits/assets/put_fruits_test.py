import sys
from unittest.mock import patch

sys.path.append("/home/labex/project")
from put_fruits import put_fruits

import unittest


def get_input(text):
    return input(text)


class TestPutFruits(unittest.TestCase):
    @patch("builtins.input", side_effect=["1.0", "2.0", "5", "10"])
    def test_put_fruits(self, mock_input):
        total, fruits = put_fruits()
        self.assertEqual(8.0, total)
        self.assertEqual([1.0, 2.0, 5], fruits)

    @patch("builtins.input", side_effect=["12"])
    def test_put_fruits_side(self, mock_input):
        total, fruits = put_fruits()
        self.assertEqual(0, total)
        self.assertEqual([], fruits)

    @patch("builtins.input", side_effect=["abc", "3", "5", "23"])
    def test_put_fruits_side_2(self, mock_input):
        total, fruits = put_fruits()
        self.assertEqual(8, total)
        self.assertEqual([3, 5], fruits)


if __name__ == "__main__":
    unittest.main()
