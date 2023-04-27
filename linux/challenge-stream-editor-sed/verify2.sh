#!/bin/zsh

if [ -f result1.txt ]; then
  result=$(diff result1.txt /tmp/verify2.txt | wc -l)
  if [ $result -eq 0 ]; then
    exit 0
  else
    exit 1
  fi
else
  exit 1
fi
