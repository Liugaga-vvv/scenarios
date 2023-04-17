#!/bin/bash

docker ps -a | grep nginx | grep my-container | grep Exited
