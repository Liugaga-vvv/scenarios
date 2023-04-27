#!/bin/zsh

minikube kubectl -- describe node minikube | grep app=prod:NoSchedule
