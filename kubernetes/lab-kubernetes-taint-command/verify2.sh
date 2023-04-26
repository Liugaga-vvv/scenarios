#!/bin/zsh

test -z "$(minikube kubectl -- describe node minikube | grep app=prod:NoSchedule)"
