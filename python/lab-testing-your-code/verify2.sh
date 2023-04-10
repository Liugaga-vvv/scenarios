#!/bin/zsh
export PYTHONPATH=${PYTHONPATH}:/home/labex/project

output=$(python3 -m unittest /home/labex/project/test_my_code.py 2>&1)

echo "$output" | grep -q -e "OK" && echo "$output" | grep -q -e "Ran 2 tests"
