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
    # TODO: implement this function
    # Note: Do not change the existing code
