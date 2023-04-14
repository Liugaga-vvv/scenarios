#!/bin/zsh

cat ~/.zsh_history | grep -q "sudo mv mytextfile.txt"

nb_files=$(ls -1 /home/labex/Desktop/challenge2 | wc -l)
if [ $nb_files -ge 2 ]; then
  exit 0
else
  exit 1
fi
