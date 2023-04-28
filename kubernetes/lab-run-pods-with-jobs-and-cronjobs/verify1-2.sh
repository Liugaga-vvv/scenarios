#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep apply | grep 'job.yaml'
minikube kubectl -- describe jobs hello-job
