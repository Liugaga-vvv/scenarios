#!/bin/bash

wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh

# init src files
touch /home/labex/project/my_code.py
touch /home/labex/project/test_my_code.py

# Install the unittest package using pip
pip install unittest

# Install the sqlite3 package using pip
pip install sqlite3

# Install sqlite3
sudo apt-get install sqlite3

# Export python path
export PYTHONPATH=${PYTHONPATH}:/home/labex/project
