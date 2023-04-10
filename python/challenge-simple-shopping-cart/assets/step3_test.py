import sys

sys.path.append("/home/labex/project")

import unittest
from shopping_cart import Product, ShoppingCart


class SecondSmallestTestCase(unittest.TestCase):
    def test_step1(self):
        cart = ShoppingCart()
        cart.add_product(Product("Apple", 0.5))
        cart.add_product(Product("Orange", 0.6))
        cart.apply_percentage_discount(10)
        self.assertLess(abs(cart.total() - 0.99), 1e-9)
        cart.apply_fixed_discount(0.2)
        self.assertLess(abs(cart.total() - 0.79), 1e-9)


if __name__ == "__main__":
    unittest.main()