#!/bin/bash

# Check if there is still a backup file from 7 days ago

RES=$(sudo find /backup -type f -name "*.tar.gz" +mtime +7 | wc -l)
if [ ${RES} -eq 0 ]; then
  echo "pass"
else
  exit 1
fi
