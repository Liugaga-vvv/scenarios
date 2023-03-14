# Querying Data

Once you have inserted data into the table, you can query it to retrieve data. Here is an example of how to query data:

```python
import sqlite3

# Create a new database
conn = sqlite3.connect('example.db')

# Query the users table
cursor = conn.execute("SELECT id, name, email, age from users")
for row in cursor:
    print(row)

# Commit the transaction
conn.commit()
```

This code queries the `users` table and prints out each row. The `SELECT` statement specifies the columns to retrieve from the table.

Then run the command below:

```bash
python3 sqlite3_programming.py
```
