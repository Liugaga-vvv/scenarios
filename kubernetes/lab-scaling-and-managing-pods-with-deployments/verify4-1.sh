#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep rollout | grep undo

IMAGE=nginx:latest

# 获取实际镜像版本
IMAGE_CURRENT=$(minikube kubectl -- get deployment my-deployment -o=jsonpath='{.spec.template.spec.containers[0].image}')

# 比较镜像版本
if [ "$IMAGE" = "$IMAGE_CURRENT" ]; then
  exit 0
else
  exit 1
fi
