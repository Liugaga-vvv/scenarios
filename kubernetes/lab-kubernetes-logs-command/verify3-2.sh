#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep nginx | grep "/bin/sh" | grep -Eq exec
