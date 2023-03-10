import sys


sys.path.append("/home/labex/project")

import unittest
from roll_dice import roll_dice

class TestRollDice(unittest.TestCase):

    def test_roll_dice(self):
        result = roll_dice()
        self.assertTrue(2 <= result <= 12)

if __name__ == '__main__':
    unittest.main()