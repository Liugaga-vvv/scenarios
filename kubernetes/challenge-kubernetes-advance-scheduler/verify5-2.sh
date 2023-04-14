#!/bin/bash

minikube kubectl -- describe pod high-request-pod | grep Status | grep Pending
