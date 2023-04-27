#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep busybox | grep nginx-busybox | grep -Eq logs
