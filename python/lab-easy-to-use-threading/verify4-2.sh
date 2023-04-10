#!/bin/zsh
# cat ~/.zsh_history | grep "thread_pool_map.py" | grep python
cd /home/labex/project
output=$(python3 thread_pool_map.py 2>&1)
echo "${output}" | grep "Hello"
