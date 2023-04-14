#!/bin/zsh
# cat ~/.zsh_history | grep "thread_subclass.py" | grep python
cd /home/labex/project
output=$(python3 thread_subclass.py 2>&1)
echo "${output}" | grep "Hello"
