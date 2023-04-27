#!/bin/zsh

test ! -z "$(minikube kubectl -- describe deployment my-deployment | grep my-annotation-key)"
