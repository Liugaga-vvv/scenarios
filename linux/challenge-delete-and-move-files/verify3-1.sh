#!/bin/zsh

# Verify that the bits mode of the file is 777
ls -ld /home/labex/Desktop/challenge3 | awk '{print $1}' | grep "rwxrwxrwx"
