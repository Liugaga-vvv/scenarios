#!/bin/zsh

FILE=~/Code/gitignore
if [ -d "$FILE" ]; then
  exit 0
else
  exit 1
fi
