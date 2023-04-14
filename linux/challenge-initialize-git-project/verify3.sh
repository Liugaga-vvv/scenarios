#!/bin/zsh

cd ~/project/gitignore

COUNT=$(git log | grep -E "^commit" | wc -l)
if [ $COUNT -eq 1 ]; then
  exit 0
else
  exit 1
fi
