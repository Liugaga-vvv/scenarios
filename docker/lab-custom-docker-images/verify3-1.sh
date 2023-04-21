#!/bin/bash

[ -f "/home/labex/docker/Dockerfile"]
grep "NGINX_PORT" /home/labex/docker/Dockerfile
