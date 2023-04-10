#!/bin/bash

(minikube kubectl -- get priorityclasses | grep low-priority) && (minikube kubectl -- get priorityclasses | grep high-priority)
