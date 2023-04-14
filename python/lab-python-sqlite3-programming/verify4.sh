#!/bin/zsh

cd /home/labex/project

output=$(python3 /home/labex/project/sqlite3_programming.py 2>&1)
# Check if we can query the data in users table
echo "$output" | grep -q 1
