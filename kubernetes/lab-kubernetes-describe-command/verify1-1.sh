#!/bin/bash

minikube kubectl -- get pod | grep "myapp-pod"
