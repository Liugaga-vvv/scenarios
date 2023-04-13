#!/bin/zsh

output=$(python3 /tmp/test_swap_dict.py 2>&1)

echo "$output" | grep -q -e "OK" && echo "$output" | grep -q -e "Ran 4 tests"
