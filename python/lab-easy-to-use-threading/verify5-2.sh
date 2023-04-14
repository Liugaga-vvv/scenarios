#!/bin/zsh
# cat ~/.zsh_history | grep "daemon_thread_with_func.py" | grep python
cd /home/labex/project
output=$(python3 daemon_thread_with_func.py 2>&1)
echo "${output}" | grep "program"
