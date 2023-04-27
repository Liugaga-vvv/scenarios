#!/bin/zsh

minikube kubectl -- get deployments | grep sample-app
