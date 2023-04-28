#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep edit
IMAGE=nginx:1.19

# 获取实际镜像版本
IMAGE_CURRENT=$(minikube kubectl -- get deployment my-deployment -o=jsonpath='{.spec.template.spec.containers[0].image}')

if [ "$IMAGE" = "$IMAGE_CURRENT" ]; then
  exit 0
else
  exit 1
fi
