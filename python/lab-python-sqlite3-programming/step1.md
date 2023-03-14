# Creating a Database

The first step in working with SQLite in Python is to create a new database. You can create a new database using the `sqlite3` module as follows:

```python
import sqlite3

# Create a new database
conn = sqlite3.connect('example.db')
```

The `connect` function creates a new database if the specified database does not exist. If the database already exists, it will connect to it. The `conn` variable represents a connection to the database.

Then run the command below:

```bash
python3 sqlite3_programming.py
```
