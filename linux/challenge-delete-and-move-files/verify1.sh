#!/bin/zsh

cat ~/.zsh_history | grep -q rm.*mytextfile.txt

cd /home/labex/Desktop/challenge1

! test -f mytextfile.txt
