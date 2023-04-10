#!/bin/zsh

cat ~/.zsh_history | grep -v "cat" | grep -iqE ";ls."
