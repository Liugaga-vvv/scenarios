#!/bin/zsh

minikube kubectl -- get clusterroles | grep myapp-admin
