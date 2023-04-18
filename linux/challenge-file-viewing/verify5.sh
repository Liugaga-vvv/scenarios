#!/bin/zsh

if [ -f step5.txt ]; then
  result=$(diff step55.txt step5.txt | wc -l)
  if [ $result -eq 0 ]; then
    exit 0
  else
    exit 1
  fi
else
  exit 1
fi
