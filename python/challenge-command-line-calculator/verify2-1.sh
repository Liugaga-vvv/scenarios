#!/bin/zsh

if ! python3 /home/labex/project/calculator.py; then
  exit 1
fi

if ! grep "add_argument" /home/labex/project/calculator.py; then
  exit 1
fi

if ! grep "\--add" /home/labex/project/calculator.py; then
  exit 1
fi

if ! grep "\--subtract" /home/labex/project/calculator.py; then
  exit 1
fi

if ! grep "\--multiply" /home/labex/project/calculator.py; then
  exit 1
fi

grep "\--divide" /home/labex/project/calculator.py
