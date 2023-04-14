#!/bin/bash

(minikube kubectl -- get clusterrole | grep prometheus) && (minikube kubectl -- get clusterrolebinding | grep prometheus)
