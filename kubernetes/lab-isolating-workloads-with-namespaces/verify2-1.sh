#!/bin/zsh

minikube kubectl -- get deployments -n webapp | grep web-app
