import sys

sys.path.append("/home/labex/project/")

from unittest.mock import patch

import unittest
from while_loop import while_loop


class TestAssignmentExpressionsChallenge(unittest.TestCase):
    @patch("builtins.input")
    def test_count_vowels(self, mock_input):

        mock_input.side_effect = ["3", "5", "7", "0"]

        self.assertEqual(while_loop(), 15)


if __name__ == "__main__":
    unittest.main()
