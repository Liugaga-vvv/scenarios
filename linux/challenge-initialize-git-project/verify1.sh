#!/bin/zsh

FILE=~/myrepo/.git
if [ -d "$FILE" ]; then
  exit 0
else
  exit 1
fi
