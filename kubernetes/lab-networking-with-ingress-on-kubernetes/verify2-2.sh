#!/bin/zsh

minikube kubectl -- get services | grep sample-app
