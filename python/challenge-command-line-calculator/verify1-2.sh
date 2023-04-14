#!/bin/zsh

if ! python3 /home/labex/project/calculator.py; then
  exit 1
fi

grep "parser.add_mutually_exclusive_group" /home/labex/project/calculator.py
