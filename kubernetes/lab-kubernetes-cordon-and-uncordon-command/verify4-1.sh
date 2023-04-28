#!/bin/bash
cat ~/.zsh_history | grep kubectl | grep label | grep nodes | grep minikube | grep 'org=labex'
