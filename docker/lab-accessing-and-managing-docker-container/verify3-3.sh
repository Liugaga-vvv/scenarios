#!/bin/bash

docker ps -a | grep ubuntu | grep my-shell-container | grep Exited
