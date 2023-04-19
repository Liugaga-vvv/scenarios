#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep service | grep myapp-service | grep -Eq describe
