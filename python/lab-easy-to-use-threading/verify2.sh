#!/bin/zsh
cat ~/.zsh_history | grep "sync.py" | grep python
cd /home/labex/project
output=$(python3 sync.py 2>&1)
echo "${output}" | grep "10"
