#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep apply | grep 'multi-pod-job.yaml'

minikube kubectl -- describe jobs download-job
