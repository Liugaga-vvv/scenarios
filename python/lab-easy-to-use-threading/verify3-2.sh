#!/bin/zsh
# cat ~/.zsh_history | grep "thread_with_args.py" | grep python
cd /home/labex/project
output=$(python3 thread_with_args.py 2>&1)
echo "${output}" | grep "1"
