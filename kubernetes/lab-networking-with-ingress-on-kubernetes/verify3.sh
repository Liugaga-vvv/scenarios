#!/bin/zsh

minikube kubectl -- get ingress | grep test-ingress
