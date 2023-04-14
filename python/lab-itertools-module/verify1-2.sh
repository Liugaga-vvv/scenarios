# cat ~/.zsh_history | grep "cycle.py"
cd /home/labex/project
output=$(python3 cycle.py 2>&1)
echo "${output}" | grep "3"
