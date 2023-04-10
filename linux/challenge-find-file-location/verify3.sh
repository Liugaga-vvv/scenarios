#!/bin/zsh

cat ~/.zsh_history | grep -iqE ";which\s+grep$"
result=$?
cat ~/.zsh_history | grep -qE ";which\s+tar$"
result1=$?
cat ~/.zsh_history | grep -iqE ";which\s+ls$"
result2=$?

if [ $result -eq 0 ] && [ $result1 -eq 0 ] && [ $result2 -eq 0 ]; then
  exit 0
else
  exit 1
fi
