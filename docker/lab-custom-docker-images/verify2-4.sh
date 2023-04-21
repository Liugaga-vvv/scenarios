#!/bin/bash
docker ps -a | grep my-nginx-curl
cat ~/.zsh_history | grep -E "docker\s+exec\s+-it\s+curl\s+bash"
