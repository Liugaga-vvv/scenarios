# cat ~/.zsh_history | grep "permutations.py"
cd /home/labex/project
output=$(python3 permutations.py 2>&1)
echo "${output}" | grep "(3, 1)"
