#!/bin/bash

# Check if the zip package exists

HOST_IP=$(sudo ifconfig | grep -v "127.0.0.1" | grep -Eo 'addr:[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
NOW_TIME=$(date "+%F")

test -f /backup/${HOST_IP}_${NOW_TIME}_linux.tar.gz
