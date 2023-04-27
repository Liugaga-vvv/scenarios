#!/bin/bash

cat ~/.zsh_history | grep -q 'kubectl\s\+logs\s\+nginx-fluentd\s\+-c\s\+nginx'
cat ~/.zsh_history | grep -q 'kubectl\s\+logs\s\+nginx-fluentd\s\+-c\s\+fluentd'
