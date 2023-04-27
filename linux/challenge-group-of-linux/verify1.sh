#!/bin/zsh

sudo cat /etc/group | grep "sales"
RS=$?
if [ $RS -eq 0 ]; then
  exit 0
else
  exit 1
fi
