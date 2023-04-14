import sqlite3


def record_order(
    cursor: sqlite3.Cursor, book_id: int, quantity: int, order_date: str
) -> None:
    """Record a new order in the 'orders' table.

    Args:
        cursor (sqlite3.Cursor): The cursor to execute the SQL command.
        book_id (int): The id of the book being ordered.
        quantity (int): The quantity of books being ordered.
        order_date (str): The date of the order in the format 'YYYY-MM-DD'.

    Returns:
        None
    """
    query = f"INSERT INTO orders (book_id, quantity, order_date) VALUES (?, ?, ?)"
    cursor.execute(query, (book_id, quantity, order_date))
