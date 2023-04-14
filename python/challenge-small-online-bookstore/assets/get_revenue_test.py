import sys

sys.path.append("/home/labex/project")

import unittest
import sqlite3
from add_book import add_book
from record_order import record_order
from get_revenue import get_revenue


class TestBookstore(unittest.TestCase):
    def setUp(self):
        # create a temporary database for testing
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()

        # create tables
        self.cursor.execute(
            "CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, price REAL)"
        )
        self.cursor.execute(
            "CREATE TABLE orders (id INTEGER PRIMARY KEY, book_id INTEGER, quantity INTEGER, order_date TEXT)"
        )

    def tearDown(self):
        # close the database connection
        self.conn.close()

    def test_get_revenue(self):
        # add some books to the 'books' table
        add_book(self.cursor, "The Great Gatsby", "F. Scott Fitzgerald", 15.99)
        add_book(self.cursor, "The Catcher in the Rye", "J.D. Salinger", 12.99)

        # record some orders in the 'orders' table
        record_order(self.cursor, 1, 2, "2023-02-21")
        record_order(self.cursor, 2, 3, "2023-02-22")

        # check that the revenue is calculated correctly
        self.assertAlmostEqual(
            get_revenue(self.cursor, "2023-02-21", "2023-02-22"), 70.95
        )


if __name__ == "__main__":
    unittest.main()
