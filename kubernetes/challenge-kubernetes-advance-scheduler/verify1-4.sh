#!/bin/bash

minikube kubectl -- describe pod my-pod | grep "Node-Selector" | grep "zoo=labex-node-selector"
