#!/bin/zsh

cat /etc/group | grep -i "devs"
result=$?

if [ $result -eq 0 ]; then
  exit 1
else
  exit 0
fi
