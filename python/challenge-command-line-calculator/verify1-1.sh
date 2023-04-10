#!/bin/zsh

if ! grep "argparse.ArgumentParser" /home/labex/project/calculator.py; then
  exit 1
fi

grep "description" /home/labex/project/calculator.py
