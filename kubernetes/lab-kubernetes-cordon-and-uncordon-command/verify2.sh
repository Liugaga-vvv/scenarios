#!/bin/bash

if cat ~/.zsh_history | grep kubectl | grep uncordon | grep minikube > /dev/null && minikube kubectl -- describe nodes | grep -E 'Unschedulable:[[:space:]]+false'; then
  history -c
  exit 0
else
  exit 1
fi
