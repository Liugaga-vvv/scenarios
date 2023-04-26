#!/bin/zsh

minikube kubectl -- get clusterrolebindings | grep myapp-admin-binding
