#!/bin/bash

FILE1=/home/labex/myvolume.tar.gz
[ -f "$FILE1" ]

sudo cp /var/lib/docker/volumes/mynewvolume/_data/hello.txt /home/labex/hello_new.txt
FILE2=/home/labex/hello_new.txt
[ -f "$FILE2" ]
