# Note

- Input `sudo mkdir /backup` command to create a new directory.
- Input `sudo ifconfig|grep -v "127.0.0.1" | grep -Eo 'addr:[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'` command to get host ip.
- Input `date "+%F"` command to get the current date.
- Input `VAR=$(ls)` command to save the output to a variable
- Input `tar -zcvf a.tar.gz b.txt` command to the packaged zip file
- Input `sh -x a.sh` command to trial run script
- Input `find ./ -type f -mtime +7 -name "*.tar.gz" | xargs rm -f` command to delete files that are 7 days old
- Input `sh a.sh` command to execution Script
- Input `crontab -e` command to add a cron job
