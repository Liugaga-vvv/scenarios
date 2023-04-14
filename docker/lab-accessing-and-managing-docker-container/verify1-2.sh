#!/bin/bash
# Check if the my-container log has been viewed
cat ~/.zsh_history | grep docker | grep my-container | grep -Eq logs
