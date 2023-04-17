#!/bin/zsh

if [ -f step3.txt ]; then
  result=$(diff step33.txt step3.txt | wc -l)
  if [ $result -eq 0 ]; then
    exit 0
  else
    exit 1
  fi
else
  exit 1
fi
