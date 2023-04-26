#!/bin/zsh

minikube kubectl -- get roles -n myapp | grep myapp-reader
