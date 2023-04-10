# cat ~/.zsh_history | grep "cr.py"
cd /home/labex/project
output=$(python3 cr.py 2>&1)
echo "${output}" | grep "(3, 3)"
