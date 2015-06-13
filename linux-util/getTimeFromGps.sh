#!/bin/bash
#ISSUE:  must return non-zero value if timeout or gps failure

#if not root, then run as root
if [ $(id -u) != "0" ]
then
    sudo "$0" "$@"
    exit $?
fi

date -s '01/01/2014 00:01'
sleep 1
pkill ntpd
pkill gpsd
gpsd -b -n -D 2 /dev/ttyUSB0
sleep 2
GPSDATE=`gpspipe -w | head -10 | grep TPV | sed -r 's/.*"time":"([^"]*)".*/\1/' | head -1`
echo $GPSDATE
date -s "$GPSDATE"
/usr/sbin/ntpd

test 'date "+%d/%m/%Y" != '01\01\2014'' && export IS_TIME_SET=true && exit 0
exit 1

