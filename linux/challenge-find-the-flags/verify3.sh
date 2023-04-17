#!/bin/zsh

FILE=~/resolve/flag3.txt
if [ -f $FILE ]; then
  exit 0
else
  exit 1
fi
