#!/bin/bash

minikube kubectl -- get configmap -n monitoring | grep prometheus-server-conf
