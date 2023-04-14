#!/bin/bash

# Check if cronjob is added

sudo crontab -l | grep '/scripts/backup-linux-log.sh'
