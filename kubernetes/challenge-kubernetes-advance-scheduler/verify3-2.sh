#!/bin/bash

pod_base=$(minikube kubectl -- describe pod pod-base | grep -w 'Node:' | awk '{print $2}')
pod_affinity=$(minikube kubectl -- describe pod pod-affinity | grep -w 'Node:' | awk '{print $2}')
[[ ${pod_base} == ${pod_affinity} ]] && echo "pass"
