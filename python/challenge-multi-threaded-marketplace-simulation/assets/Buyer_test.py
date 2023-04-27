import sys

sys.path.append("/home/labex/project")

import unittest
from Buyer import Product, Buyer
from Catalog import Catalog
from Seller import Seller

class TestSellerAndBuyer(unittest.TestCase):
    def test_seller_buyer_interaction(self):
        catalog = Catalog()
        seller = Seller(1, catalog)
        buyer = Buyer(1, catalog)

        # Seller adds products to the catalog
        products = [Product(i, f"Product {i}", i * 10.0) for i in range(1, 4)]
        for product in products:
            seller.add_product(product)

        # Buyer browses the catalog and purchases products
        catalog_products = buyer.browse_catalog()
        self.assertEqual(len(catalog_products), len(products))
        for product in catalog_products:
            buyer.buy_product(product.id)

        # Ensure catalog is empty after all products are purchased
        self.assertEqual(len(catalog.browse_catalog()), 0)

if __name__ == "__main__":
    unittest.main()