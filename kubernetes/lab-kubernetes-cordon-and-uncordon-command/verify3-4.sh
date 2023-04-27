#!/bin/bash

if cat ~/.zsh_history | grep kubectl | grep uncordon | grep minikube > /dev/null && minikube kubectl -- get pods nginx | grep Running; then
  history -c
  exit 0
else
  exit 1
fi
