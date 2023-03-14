# Deleting Data

You can also delete data from the table by using a DELETE statement. Here is an example of how to delete data:

```python
import sqlite3

# Create a new database
conn = sqlite3.connect('example.db')

# Delete data from the users table
conn.execute("DELETE FROM users WHERE name = 'Jane Doe'")

# Commit the transaction
conn.commit()
```

This code deletes the row with `name` equals to `'Jane Doe'` from the `users` table. The `DELETE FROM` statement specifies the table name and the condition for deleting rows.

Then run the command below:

```bash
python3 sqlite3_programming.py
```
