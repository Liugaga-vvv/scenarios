import sys


sys.path.append("/home/labex/project")
from basket_weight import basket_weight

import unittest


class TestBasketWeight(unittest.TestCase):
    def test_basket_weight(self):
        baskets = {}
        result = basket_weight(baskets)
        self.assertTrue(not result)
        self.assertEqual([], result)

        baskets = {"apple": [1, 2.3, 4, 5], "orange": [3], "banana": [4, 5, 6]}
        result = basket_weight(baskets)
        self.assertEqual(3, len(result))
        self.assertEqual(15, result[0]["weight"])
        self.assertEqual("banana", result[0]["name"])
        self.assertEqual(12.3, result[1]["weight"])
        self.assertEqual("apple", result[1]["name"])
        self.assertEqual(3, result[2]["weight"])
        self.assertEqual("orange", result[2]["name"])


if __name__ == "__main__":
    unittest.main()
