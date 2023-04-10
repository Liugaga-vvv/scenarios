#!/bin/bash

docker ps -a | grep web4 || echo "ok"
