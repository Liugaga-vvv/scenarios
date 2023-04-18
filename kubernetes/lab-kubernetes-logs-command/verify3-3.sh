#!/bin/zsh

minikube kubectl -- logs nginx-busybox | grep "127.0.0.1"
