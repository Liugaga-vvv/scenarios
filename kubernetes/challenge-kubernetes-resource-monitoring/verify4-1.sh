#!/bin/bash

minikube kubectl -- get service -n monitoring | grep prometheus-service | grep 30000
