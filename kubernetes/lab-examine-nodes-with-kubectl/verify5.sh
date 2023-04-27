#!/bin/zsh
cat ~/.zsh_history | grep kubectl | grep events | grep field-selector
