# Record Order

In this step, you should complete a function `record_order` in `record_order.py` to perform the following operation: Record a new order in the `orders` table.

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

# Update the price of a book
update_price(c, 'The Great Gatsby', 19.99)

# Record a new order
record_order(c, 1, 3, '2023-02-22')

# Close the database connection
conn.close()
```
