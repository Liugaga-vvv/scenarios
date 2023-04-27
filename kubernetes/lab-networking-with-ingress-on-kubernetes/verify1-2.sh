#!/bin/zsh

minikube kubectl -- get pods -n ingress-nginx | grep ingress-nginx-controller
