#!/bin/zsh

minikube kubectl -- describe node minikube | grep app=dev:NoSchedule
