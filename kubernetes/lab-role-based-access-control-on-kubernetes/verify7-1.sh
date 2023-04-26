#!/bin/zsh

minikube kubectl -- get pods -n myapp | grep myapp-pod

cat ~/.zsh_history | grep "apply.*myapp-pod.yaml.*cluster-admin"
