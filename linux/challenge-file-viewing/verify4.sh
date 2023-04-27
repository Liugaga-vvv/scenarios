#!/bin/zsh

if [ -f step4.txt ]; then
  result=$(diff step44.txt step4.txt | wc -l)
  if [ $result -eq 0 ]; then
    exit 0
  else
    exit 1
  fi
else
  exit 1
fi
