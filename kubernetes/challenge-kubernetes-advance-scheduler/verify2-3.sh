#!/bin/bash

minikube kubectl -- get pod | grep "my-affinity-pod" | grep "Running"
