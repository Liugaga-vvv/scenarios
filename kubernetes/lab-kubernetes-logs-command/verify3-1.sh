#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep nginx-busybox | grep f | grep -Eq logs
