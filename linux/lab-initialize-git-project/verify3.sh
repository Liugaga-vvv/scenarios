#!/bin/zsh

fileCount=$(find ~/myrepo/ -name "*.git" | wc -l)
if [ $fileCount -gt 1 ]; then
  exit 0
else
  exit 1
fi
