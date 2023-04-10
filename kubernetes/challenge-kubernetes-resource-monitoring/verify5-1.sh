#!/bin/bash

minikube kubectl -- get pod -n monitoring | grep grafana
