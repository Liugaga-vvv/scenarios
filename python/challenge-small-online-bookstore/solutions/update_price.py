import sqlite3


def update_price(cursor: sqlite3.Cursor, title: str, new_price: float) -> None:
    """Update the price of a book in the 'books' table.

    Args:
        cursor (sqlite3.Cursor): The cursor to execute the SQL command.
        title (str): The title of the book.
        new_price (float): The new price of the book.

    Returns:
        None
    """
    query = f"UPDATE books SET price = ? WHERE title = ?"
    cursor.execute(query, (new_price, title))
