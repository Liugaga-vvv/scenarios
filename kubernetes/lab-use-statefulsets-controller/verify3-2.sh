#!/bin/zsh

minikube kubectl -- describe pod web-0 | grep nginx:1.20.0
