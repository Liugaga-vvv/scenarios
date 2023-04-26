#!/bin/zsh

minikube kubectl -- get deployments -n myapp | grep myapp-deployment

cat ~/.zsh_history | grep -E "kubectl\s+apply\s+-f\s+myapp-deployment.yaml\s+--as\s+cluster-admin"
