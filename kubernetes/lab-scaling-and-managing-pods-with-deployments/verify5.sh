#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep delete | grep deployment | grep my-deployment
