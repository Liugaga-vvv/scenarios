import sys

sys.path.append("/home/labex/project")

import unittest
from Seller_Buyer import Seller,Buyer,Product
from Catalog import Catalog

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

class TestThreading(unittest.TestCase):
    def test_multiple_sellers_and_buyers(self):
        catalog = Catalog()
        sellers = [Seller(i, catalog) for i in range(1, 4)]
        buyers = [Buyer(i, catalog) for i in range(1, 4)]

        # Sellers add products to the catalog simultaneously
        for seller in sellers:
            seller.start()

        for seller in sellers:
            seller.join()

        catalog_products = catalog.browse_catalog()
        self.assertEqual(len(catalog_products), 3)

        # Buyers purchase products from the catalog simultaneously
        for buyer in buyers:
            buyer.start()

        for buyer in buyers:
            buyer.join()

        # Ensure catalog is empty after all products are purchased
        self.assertEqual(len(catalog.browse_catalog()), 0)

if __name__ == "__main__":
    unittest.main()