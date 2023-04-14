#!/bin/bash

mkdir myrepo
cd myrepo
echo "Hello, world!" > myfile.txt
git init
git config --global user.email "labex@example.com"
git config --global user.name "labex"
git add myfile.txt
git commit -m "Initial commit"
