#!/bin/bash

# Create the users temporary directory (logs, etc)
mkdir -p /home/pi/tmp
chown pi /home/pi/tmp
chmod 755 /home/pi/tmp

# Install the cronjob to cron.d to start watchdog at boot
FILE="/etc/cron.d/ledaKeepAlive"
cat /dev/null > $FILE  #empty file, if it exists
echo "@reboot   pi sh /home/pi/project-leda/keepalive.sh > /home/pi/tmp/keepalive.log" >> $FILE
echo "" >> $FILE

