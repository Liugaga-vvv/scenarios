#!/bin/bash

minikube kubectl -- describe pod pod-base | grep "Labels" | grep "app=pod-base"
