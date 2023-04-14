import sys

sys.path.append("/home/labex/project")

import unittest
import sqlite3
from add_book import add_book


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

    def test_add_book(self):
        # add a book to the 'books' table
        add_book(self.cursor, "The Great Gatsby", "F. Scott Fitzgerald", 15.99)

        # check that the book has been added
        self.cursor.execute(
            "SELECT * FROM books WHERE title = ?", ("The Great Gatsby",)
        )
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], "The Great Gatsby")
        self.assertEqual(result[2], "F. Scott Fitzgerald")
        self.assertEqual(result[3], 15.99)


if __name__ == "__main__":
    unittest.main()
