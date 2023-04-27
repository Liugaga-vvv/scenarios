#!/bin/zsh

minikube kubectl -- get services -n webapp | grep web-app
