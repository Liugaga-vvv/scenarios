# cat ~/.zsh_history | grep "product.py"
cd /home/labex/project
output=$(python3 product.py 2>&1)
echo "${output}" | grep "(2"
