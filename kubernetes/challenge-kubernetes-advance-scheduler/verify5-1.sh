#!/bin/bash

minikube kubectl -- get pod low-request-pod | grep "Running"
