#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep apply

minikube kubectl -- describe deployment nginx-deployment
