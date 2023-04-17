#!/bin/bash
cat ~/.zsh_history | grep docker | grep my-shell-container | grep -Eq rm
if docker ps -a | grep -Eq my-shell-container; then
  exit 1
else
  exit 0
fi
