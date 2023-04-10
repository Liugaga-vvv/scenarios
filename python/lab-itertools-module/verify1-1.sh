# cat ~/.zsh_history | grep "chain.py"
cd /home/labex/project
output=$(python3 chain.py 2>&1)
echo "${output}" | grep "a"
