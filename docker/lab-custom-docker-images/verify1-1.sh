#!/bin/zsh

[ -f "/home/labex/docker/Dockerfile"]
grep -E "nginx|index.html" /home/labex/docker/Dockerfile
