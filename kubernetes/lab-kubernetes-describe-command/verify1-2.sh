#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep pod | grep myapp-pod | grep -Eq describe
