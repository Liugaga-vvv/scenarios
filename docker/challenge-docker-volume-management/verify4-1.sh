#!/bin/bash

test -d /tmp/share
if [ $? -eq 0 ]; then
  docker ps | grep nginx-share
fi
