#!/bin/zsh

output=$(python3 /tmp/age_unittest.py 2>&1)

echo "$output" | grep -q -e "OK" && echo "$output" | grep -q -e "Ran 3 tests"
