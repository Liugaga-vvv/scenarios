#!/bin/bash

docker ps -a | grep c1
cat ~/.zsh_history | grep -E "docker\s+inspect\s+c1"
