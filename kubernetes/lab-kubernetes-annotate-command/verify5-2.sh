#!/bin/zsh

minikube kubectl -- get deployments | grep my-deployment
