#!/bin/zsh

cd ~/myrepo
git status | grep -iqE "^Changes\s+to\s+be\s+committed"
