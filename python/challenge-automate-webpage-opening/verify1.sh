#!/bin/zsh

# Check if the file /home/labex/project/webbrowser_challenge.py contains the key strings.

if ! grep "ArgumentParser" /home/labex/project/webbrowser_challenge.py; then
  exit 1
fi

if ! grep "parse_args" /home/labex/project/webbrowser_challenge.py; then
  exit 1
fi

if ! grep "open_new" /home/labex/project/webbrowser_challenge.py; then
  exit 1
fi

# Check if the browser is running.

ps -A | grep "browser"
