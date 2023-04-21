#!/bin/bash

minikube kubectl -- get deployment | grep "myapp-deployment"
