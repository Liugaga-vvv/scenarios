import sys

sys.path.append("/home/labex/project")

import unittest
from Product import Product

class TestProduct(unittest.TestCase):
    def test_init(self):
        product = Product(1, "Test Product", 10.99)
        self.assertEqual(product.id, 1)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 10.99)
if __name__ == "__main__":
    unittest.main()