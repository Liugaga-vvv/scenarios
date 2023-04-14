#!/bin/bash

minikube kubectl -- describe node minikube | grep Taint | grep "NoSchedule"
