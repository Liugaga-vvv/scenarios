# Add Book

In this step, you should complete a function `add_book` in `add_book.py` to perform the following operation: Add a new book to the `books` table.

## Example Usage

Here is an example of how your program could be used:

```python
# Import the necessary modules
import sqlite3

# Connect to the database
conn = sqlite3.connect('bookstore.db')
c = conn.cursor()

# Add a new book
add_book(c, 'The Great Gatsby', 'F. Scott Fitzgerald', 15.99)

# Close the database connection
conn.close()
```
