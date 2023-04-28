#!/bin/zsh
minikube kubectl -- get node minikube --show-labels | grep org=labex
