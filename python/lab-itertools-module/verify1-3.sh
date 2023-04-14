# cat ~/.zsh_history | grep "count.py"
cd /home/labex/project
output=$(python3 count.py 2>&1)
echo "${output}" | grep "14"
