import sys

sys.path.append("/home/labex/project")

import unittest
from calculate_winner import calculate_winner


class TestCalculateWinner(unittest.TestCase):
    def test_calculate_winner(self):
        votes = ["john", "John", "Mary", "mary", "Peter", "PETER", "john"]
        self.assertEqual(calculate_winner(votes), "John")

        votes = ["john", "Mary", "peter", "Peter", "mary"]
        self.assertEqual(calculate_winner(votes), "Tie")


if __name__ == "__main__":
    unittest.main()
