#!/bin/bash

minikube kubectl -- get service -n monitoring | grep grafana | grep 32000
