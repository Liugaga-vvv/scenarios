#!/bin/bash

replicas=$(minikube kubectl -- get po | grep helloworld | grep Running | wc -l)
[ ${replicas} -eq 5 ] && echo "pass"
