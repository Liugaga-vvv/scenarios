#!/bin/bash

# Check if the test.txt file created in data volume
sudo test -f /var/lib/docker/volumes/my-vol/_data/test.txt
