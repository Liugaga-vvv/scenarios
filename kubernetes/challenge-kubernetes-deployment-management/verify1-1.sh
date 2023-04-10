#!/bin/bash

minikube kubectl -- run -it --rm --image=mysql:5.7 --restart=Never mysql-client -- mysql -h mysql -proot -e "show databases;" | grep "hello-world"
