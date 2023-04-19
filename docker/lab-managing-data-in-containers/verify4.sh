#!/bin/bash
cat ~/.zsh_history | grep -E "docker\s+exec\s+c1\s+cat\s+/app/data/hello.txt"
