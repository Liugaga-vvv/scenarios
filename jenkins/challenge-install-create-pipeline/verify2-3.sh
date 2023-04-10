#!/bin/bash

q=$(ls -l /opt/tomcat | sed -n '2p' | awk -F " " '{print $3}')
if [ "${q}" == "tomcat" ]; then
  echo "pass"
fi
