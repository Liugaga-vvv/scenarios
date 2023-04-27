#!/bin/bash

if grep -q "postgres://newuser:newpassword@newhost:newport/newdbname" "/home/labex/project/configmap.yaml"; then
  exit 0
else
  exit 1
fi
