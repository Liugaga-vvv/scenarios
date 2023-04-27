#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep deployment | grep restart | grep rollout
