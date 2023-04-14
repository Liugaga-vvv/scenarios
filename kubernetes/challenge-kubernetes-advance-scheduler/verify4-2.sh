#!/bin/bash

minikube kubectl -- get deployment low-priority-pods -oyaml | grep "low-priority"
