#!/bin/zsh

id john | grep "sales"
RS=$?
id jane | grep "sales"
RS1=$?
if [ $RS -eq 0 ] && [ $RS1 -eq 0 ]; then
  exit 0
else
  exit 1
fi
