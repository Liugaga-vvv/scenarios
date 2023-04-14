#!/bin/zsh

FILE=~/myrepo/newfile.txt
if [ -f "$FILE" ]; then
  result=1
else
  result=0
fi

cat ~/.zsh_history | grep -qE ";git\s+rm"
result1=$?

if [ $result -eq 0 ] && [ $result1 -eq 0 ]; then
  exit 0
else
  exit 1
fi
