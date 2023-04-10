#!/bin/zsh
# cat ~/.zsh_history | grep "timer_object.py" | grep python
cd /home/labex/project
output=$(python3 timer_object.py 2>&1)
echo "${output}" | grep "timer"
