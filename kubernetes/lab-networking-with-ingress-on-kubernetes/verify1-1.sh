#!/bin/zsh

minikube kubectl -- get namespaces | grep ingress-nginx
