#!/bin/zsh

cd ~/myrepo
git status | grep -iqE "^nothing\s+to\s+commit"
