#!/bin/zsh
sudo grep "document_root\$fastcgi_script_name" /etc/nginx/sites-available/default \
  && sudo nginx -t
