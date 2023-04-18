#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep deployment | grep myapp-deployment | grep -Eq describe
