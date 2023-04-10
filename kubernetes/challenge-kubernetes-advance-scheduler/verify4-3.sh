#!/bin/bash

minikube kubectl -- get deployment high-priority-pods -oyaml | grep "high-priority"
