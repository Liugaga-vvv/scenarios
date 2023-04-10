#!/bin/bash

test -f /tmp/share/share.txt
if [ $? -eq 0 ]; then
  docker exec -it nginx-share cat /usr/share/nginx/html/share.txt \
    && docker exec -it busybox-share cat /usr/share/nginx/html/share.txt
fi
