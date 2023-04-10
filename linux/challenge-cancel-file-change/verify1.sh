#!/bin/zsh

md5sum ~/myrepo/myfile.txt | grep -iqE "^746308829575e17c3331bbcb00c0898b"
result=$?
cat ~/.zsh_history | grep -qE ";git\s+restore"
result1=$?
if [ $result -eq 0 ] && [ $result1 -eq 0 ]; then
  exit 0
else
  exit 1
fi
