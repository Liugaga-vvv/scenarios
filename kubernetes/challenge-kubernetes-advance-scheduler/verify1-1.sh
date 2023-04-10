#!/bin/bash

minikube kubectl -- get node --show-labels | grep "labex-node-selector"
