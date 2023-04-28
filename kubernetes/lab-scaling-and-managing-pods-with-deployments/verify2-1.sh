#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep scale

REPLICAS_DESIRED=5

# 获取实际副本数
REPLICAS_CURRENT=$(minikube kubectl -- get deployment my-deployment -o=jsonpath='{.spec.replicas}')

# 比较副本数
if [ "$REPLICAS_DESIRED" -eq "$REPLICAS_CURRENT" ]; then
  exit 0
else
  exit 1
fi
