#!/bin/zsh

test ! -z "$(minikube kubectl -- describe pod my-pod | grep my-annotation-key-1)"
test ! -z "$(minikube kubectl -- describe pod my-pod | grep my-annotation-key-2)"
