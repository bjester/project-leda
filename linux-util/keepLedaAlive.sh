#!/bin/bash
# Make sure that ntp server syncs to real-time clock and that project-leda is running

if [ $IS_TIME_SET == false ]
then
    ./getTimeFromGps.sh  #ISSUE:  will Not timeout if gps is disconnected
    if [ $? -ne 0 ]
    then
        echo "NTP could not sync with real-time clock"
    else
        #check that pidof returns success signal    
        pidof main.py
        if [ $? -ne 0 ]
        then
            echo 'launching Project Leda'
            ~/project-leda/main.py
        fi
    fi
fi



