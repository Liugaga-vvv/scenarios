#!/bin/zsh

cat ~/.zsh_history | grep -iqE ";locate\s+report$"
result=$?
cat ~/.zsh_history | grep -iqE ";locate\s+\*\.docx$"
result1=$?

if [ $result -eq 0 ] && [ $result1 -eq 0 ]; then
  exit 0
else
  exit 1
fi
