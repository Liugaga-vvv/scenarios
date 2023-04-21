#!/bin/zsh

docker ps -a | grep myapp
grep -E "docker|run|myapp" ~/.zsh_history
