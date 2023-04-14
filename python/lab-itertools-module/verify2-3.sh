# cat ~/.zsh_history | grep "combinations.py"
cd /home/labex/project
output=$(python3 combinations.py 2>&1)
echo "${output}" | grep "(1, 3)"
