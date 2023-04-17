#!/bin/bash
# Check if the my-container container start.
docker ps -a | grep nginx | grep my-container | grep Up
