import sys

sys.path.append("/home/labex/project")

import unittest
from shopping_cart import Product, ShoppingCart


class SecondSmallestTestCase(unittest.TestCase):
    def test_step1(self):
        cart = ShoppingCart()
        cart.add_product(Product("Apple", 0.5))
        cart.add_product(Product("Orange", 0.6))
        self.assertLess(abs(cart.total() - 1.1), 1e-9)
        cart.remove_product("Apple")
        self.assertLess(abs(cart.total() - 0.6), 1e-9)


if __name__ == "__main__":
    unittest.main()
