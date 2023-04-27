#!/bin/zsh
minikube kubectl -- describe node minikube | grep Taints | grep app=backend
