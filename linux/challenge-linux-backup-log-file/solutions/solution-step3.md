# Note

1. Input `sudo vim /scripts/backup-linux-log.sh` command to create a backup script file and write the actions with the following content.

```bash
#!/bin/bash
HOST_IP=$(sudo ifconfig | grep -v "127.0.0.1" | grep -Eo 'addr:[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
NOW_TIME=$(date "+%F")
sudo tar -zcvf /backup/${HOST_IP}_${NOW_TIME}_linux.tar.gz /var/log/dmesg /var/log/faillog /var/log/lastlog
sudo find /backup/ -type f -mtime +7 -name "*.tar.gz" | xargs rm -f
```

3. Input `sh -x /scripts/backup-linux-log.sh` command to check the script syntax for problems.
4. Input `sh /scripts/backup-linux-log.sh` command to execute the script to see if creating the backup file is successful.
