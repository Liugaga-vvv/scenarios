#!/bin/bash

minikube kubectl -- get service | grep "myapp-service"
