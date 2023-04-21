#!/bin/zsh

sudo cat /etc/group | grep "sales"
RS=$?
if [ $RS -eq 0 ]; then
  exit 1
else
  exit 0
fi
