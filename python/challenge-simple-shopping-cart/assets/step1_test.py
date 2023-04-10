import sys

sys.path.append("/home/labex/project")

import unittest
from shopping_cart import Product


class SecondSmallestTestCase(unittest.TestCase):
    def test_step1(self):
        product = Product("Apple", 0.5)
        self.assertEqual(product.name, "Apple")
        self.assertEqual(product.price, 0.5)


if __name__ == "__main__":
    unittest.main()
