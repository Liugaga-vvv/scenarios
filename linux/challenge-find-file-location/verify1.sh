#!/bin/zsh

cat ~/.zsh_history | grep -iqE ";find\s+\.\s+\-name\s+\"\*\.txt\""
result=$?
cat ~/.zsh_history | grep -qE ";find +\.\s+\-size\s+\+1M"
result1=$?
cat ~/.zsh_history | grep -iqE ";find +\.\s+\-mtime\s+\-7"
result2=$?

if [ $result -eq 0 ] && [ $result1 -eq 0 ] && [ $result2 -eq 0 ]; then
  exit 0
else
  exit 1
fi
