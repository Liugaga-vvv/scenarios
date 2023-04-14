#!/bin/zsh

# Check if there is at least one user calles Jane Doe in the users table
sqlite3 /home/labex/project/example.db "SELECT * FROM users WHERE name='Jane Doe';" | grep -q Jane
