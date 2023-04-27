import sys

sys.path.append("/home/labex/project")

import unittest
from Catalog import Product, Catalog

class TestCatalog(unittest.TestCase):
    def test_add_product(self):
        catalog = Catalog()
        product = Product(1, "Test Product", 20.0)
        catalog.add_product(product)
        self.assertEqual(catalog.get_product(1), product)

    def test_remove_product(self):
        catalog = Catalog()
        product = Product(1, "Test Product", 20.0)
        catalog.add_product(product)
        catalog.remove_product(1)
        self.assertIsNone(catalog.get_product(1))

    def test_browse_catalog(self):
        catalog = Catalog()
        products = [Product(i, f"Product {i}", i * 10.0) for i in range(1, 4)]
        for product in products:
            catalog.add_product(product)
        catalog_products = catalog.browse_catalog()
        self.assertEqual(len(catalog_products), len(products))
        for product in products:
            self.assertIn(product, catalog_products)

if __name__ == "__main__":
    unittest.main()