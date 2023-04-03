#!/bin/zsh

cat ~/.zsh_history | grep -q "mv mytextfile.txt"

cd /home/labex/Desktop/challenge3

! test -f mytextfile.txt
