#!/bin/zsh
# cat ~/.zsh_history | grep "create_thread.py" | grep python
cd /home/labex/project
output=$(python3 create_thread.py 2>&1)
echo "${output}" | grep "Hello"
