#!/bin/zsh
minikube kubectl -- describe node minikube | grep -i Annotations: | grep production
