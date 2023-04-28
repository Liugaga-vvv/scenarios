#!/bin/zsh

minikube kubectl -- get pvc my-pvc | grep 1Gi
