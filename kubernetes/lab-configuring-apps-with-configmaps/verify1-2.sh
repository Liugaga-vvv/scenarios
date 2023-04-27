#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep apply
minikube kubectl -- describe configmap my-config
