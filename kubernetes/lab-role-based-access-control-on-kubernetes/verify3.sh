#!/bin/zsh

minikube kubectl -- get rolebindings -n myapp | grep myapp-reader-binding
