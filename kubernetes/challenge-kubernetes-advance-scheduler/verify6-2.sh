#!/bin/bash

minikube kubectl -- get pod pod-not-tolerate | grep "Pending"
