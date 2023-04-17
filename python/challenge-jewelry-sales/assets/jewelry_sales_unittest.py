import unittest
import sys

sys.path.append("/home/labex/project")
from jewelry_sales import process_sales_data


class TestProcessSalesData(unittest.TestCase):
    def test_empty_sales_list(self):
        sales = []
        result = process_sales_data(sales)
        self.assertEqual(result, (0.0, 0, 0.0, ""))

    def test_one_sale(self):
        sales = [("Necklace", 1, 15.50)]
        result = process_sales_data(sales)
        self.assertEqual(result, (15.50, 1, 15.50, "Necklace"))

    def test_multiple_sales_same_product(self):
        sales = [("Earrings", 2, 10.00), ("Earrings", 1, 10.00), ("Earrings", 3, 10.00)]
        result = process_sales_data(sales)
        self.assertEqual(result, (60.00, 6, 10.00, "Earrings"))

    def test_multiple_sales_different_products(self):
        sales = [("Bracelet", 1, 12.00), ("Earrings", 2, 8.50), ("Necklace", 3, 20.00)]
        result = process_sales_data(sales)
        self.assertEqual(result, (89.0, 6, 14.83, "Necklace"))

    def test_sales_with_negative_quantity(self):
        sales = [("Bracelet", 1, 12.00), ("Earrings", -2, 8.50), ("Necklace", 3, 20.00)]
        with self.assertRaises(ValueError):
            process_sales_data(sales)

    def test_sales_with_negative_price(self):
        sales = [("Bracelet", 1, 12.00), ("Earrings", 2, -8.50), ("Necklace", 3, 20.00)]
        with self.assertRaises(ValueError):
            process_sales_data(sales)


if __name__ == "__main__":
    unittest.main()
