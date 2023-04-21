#!/bin/zsh

if [ -f step2.txt ]; then
  result=$(diff step22.txt step2.txt | wc -l)
  if [ $result -eq 0 ]; then
    exit 0
  else
    exit 1
  fi
else
  exit 1
fi
