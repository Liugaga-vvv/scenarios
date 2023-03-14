# Updating Data

You can also update existing data in the table by using an `UPDATE` statement. Here is an example of how to update data:

```python
import sqlite3

# Create a new database
conn = sqlite3.connect('example.db')

# Update data in the users table
conn.execute("UPDATE users SET age = 40 WHERE name = 'Jane Doe'")

# Commit the transaction
conn.commit()
```

This code updates the `age` column for the row with `name` equals to `'Jane Doe'`. The `UPDATE` statement specifies the table name, the column to update, and the new value.

Then run the command below:

```bash
python3 sqlite3_programming.py
```
