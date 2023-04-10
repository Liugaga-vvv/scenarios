import sys

sys.path.append("/home/labex/project")

import unittest
import sqlite3
from add_book import add_book
from record_order import record_order


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

    def test_record_order(self):
        # add a book to the 'books' table
        add_book(self.cursor, "The Great Gatsby", "F. Scott Fitzgerald", 15.99)

        # record a new order in the 'orders' table
        record_order(self.cursor, 1, 3, "2023-02-22")

        # check that the order has been recorded
        self.cursor.execute("SELECT * FROM orders WHERE book_id = ?", (1,))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 3)
        self.assertEqual(result[3], "2023-02-22")


if __name__ == "__main__":
    unittest.main()
