#!/bin/zsh

# Store the output of the grep command in a variable
nargs=$(grep -c "nargs" /home/labex/project/calculator.py)
type=$(grep -c "type" /home/labex/project/calculator.py)
metavar=$(grep -c "metavar" /home/labex/project/calculator.py)
help=$(grep -c "help" /home/labex/project/calculator.py)

# Check if the nargs is less than 4
if [ $nargs -lt 4 ]; then
  exit 1
fi

# Check if the type is less than 4
if [ $type -lt 4 ]; then
  exit 1
fi

# Check if the metavar is less than 4
if [ $metavar -lt 4 ]; then
  exit 1
fi

# Check if the help is less than 4
if [ $help -lt 4 ]; then
  exit 1
fi
