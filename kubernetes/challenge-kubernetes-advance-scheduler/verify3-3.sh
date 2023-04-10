#!/bin/bash

minikube kubectl -- get pod pod-anti-affinity | grep -w "Pending"
