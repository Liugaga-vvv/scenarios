#!/bin/zsh

minikube kubectl -- get statefulset web | grep 5/5
