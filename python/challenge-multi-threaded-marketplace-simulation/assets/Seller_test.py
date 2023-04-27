import sys

sys.path.append("/home/labex/project")

import unittest
from Seller import Catalog, Seller
from Buyer import Buyer

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
        self.assertEqual(len(catalog_products), 9)

        # Buyers purchase products from the catalog simultaneously
        for buyer in buyers:
            buyer.start()

        for buyer in buyers:
            buyer.join()

        # Ensure catalog is empty after all products are purchased
        self.assertEqual(len(catalog.browse_catalog()), 0)

if __name__ == "__main__":
    unittest.main()