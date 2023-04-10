#!/bin/bash

minikube kubectl -- get pod pod-tolerate | grep "Running"
