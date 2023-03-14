#!/bin/zsh

# Check if the age of Jane Doe is updated to 40
sqlite3 /home/labex/project/example.db "SELECT * FROM users WHERE name='Jane Doe' AND age=40;" | grep -q "|40"
