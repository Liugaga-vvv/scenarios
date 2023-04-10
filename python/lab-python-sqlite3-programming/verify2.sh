#!/bin/zsh

# Check if the table users exists in example.db
sqlite3 /home/labex/project/example.db "SELECT name FROM sqlite_master WHERE type='table' AND name='users';" | grep -q users
