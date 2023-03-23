# Creating a Table

Once you have created a new database, you can create a table to store data in. Here is an example of how to create a table:

```python
import sqlite3

# Create a new database
conn = sqlite3.connect('example.db')

# Create a new table
conn.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY,
              name TEXT NOT NULL,
              email TEXT NOT NULL,
              age INTEGER);''')

# Commit the transaction
conn.commit()
```

This code creates a new table called `users` with four columns: `id`, `name`,`email`, and `age`. The `id` column is the primary key, which means that it is unique for each row and is used to identify each row in the table.

Then run the command below:

```bash
python3 sqlite3_programming.py
```
