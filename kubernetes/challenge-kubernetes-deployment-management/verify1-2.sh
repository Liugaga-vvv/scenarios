#!/bin/bash

minikube kubectl -- get pod | grep 'helloworld' | grep Running
