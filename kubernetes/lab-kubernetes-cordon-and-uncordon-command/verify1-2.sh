#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep cordon | grep minikube
minikube kubectl -- describe nodes | grep -E 'Unschedulable:[[:space:]]+true'
