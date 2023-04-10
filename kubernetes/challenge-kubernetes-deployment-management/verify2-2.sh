#!/bin/bash

node_ip=$(minikube kubectl -- get node -o wide | grep minikube | awk '{print $6}')
curl ${node_ip}:31323 | grep "Kubernetes"
