#!/bin/bash

[ -f "/home/labex/myapp/Dockerfile" ]

grep -E "node:14-alpine|RUN|3000|WORKDIR|EXPOSE|CMD" /home/labex/myapp/Dockerfile
