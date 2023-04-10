#!/bin/zsh
# cat ~/.zsh_history | grep "event_object.py" | grep python
cd /home/labex/project
output=$(python3 event_object.py 2>&1)
echo "${output}" | grep "received"
