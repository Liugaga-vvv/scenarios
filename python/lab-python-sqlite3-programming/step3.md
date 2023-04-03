# Inserting Data

After you have created a table, you can start inserting data into it. Here is an example of how to insert data:

```python
import sqlite3

# Create a new database
conn = sqlite3.connect('example.db')

# Insert data into the users table
conn.execute("INSERT INTO users (name, email, age) VALUES ('John Doe', 'john@example.com', 30)")
conn.execute("INSERT INTO users (name, email, age) VALUES ('Jane Doe', 'jane@example.com', 25)")

# Commit the transaction
conn.commit()
```

This code inserts two new rows into the `users` table. The `INSERT INTO` statement specifies the table name and the values to insert into the table.

Then run the command below:

```bash
python3 sqlite3_programming.py
```
