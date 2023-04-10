# Note

- Input `sudo ifconfig|grep -v "127.0.0.1" | grep -Eo 'addr:[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'` command to get host ip.
- Input `HOST_IP=172.18.0.5` command to set the `HOST_IP` variable. You should change the IP address.
- Input `date "+%F"` command to get the current date.
- Input `NOW_TIME=2022-12-13` command to set the `NOW_TIME` variable.
- Input `sudo tar -zcvf /backup/${HOST_IP}_${NOW_TIME}_linux.tar.gz /var/log/dmesg /var/log/faillog /var/log/lastlog` command to the packaged zip file.
- Input `find /backup/ -type f -mtime +7 -name "*.tar.gz" | xargs rm -f` command to delete files that are `7 days old`.
