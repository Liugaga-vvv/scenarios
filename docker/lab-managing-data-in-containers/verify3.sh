#!/bin/bash
sudo cp /var/lib/docker/volumes/myvolume/_data/hello.txt /home/labex/hello.txt
FILE=/home/labex/hello.txt
[ -f "$FILE" ]

cat ~/.zsh_history | grep -E "docker\s+exec\s+c1\s+sh\s+-c"
cat ~/.zsh_history | grep -E "docker\s+volume\s+inspect\s+myvolume"
