#!/bin/bash

[ -f "/home/labex/docker/index.html" ]
grep -E "DOCTYPE|html|head|title|Hello|Docker|body" /home/labex/docker/index.html
