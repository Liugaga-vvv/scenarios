#!/bin/zsh

output=$(python3 -m unittest /home/labex/project/calculator_unittest.py 2>&1)

echo "$output" | grep -q -e "OK" && echo "$output" | grep -q -e "Ran 4 tests"
