#!/bin/bash



PIDFILE="$HOME/tmp/leda.pid"

while true
do
    if [ -e "${PIDFILE}" ] && (ps -u $(whoami) -opid= |
        grep -P "^\s*$(cat ${PIDFILE})$" &> /dev/null); then
        echo "Already running."
    else 
        $HOME/project-leda/main.py > $HOME/tmp/leda.log &
        echo $! > "${PIDFILE}"
        chmod 644 "${PIDFILE}"
        echo "Watchdog restarting LEDA"
    fi
    sleep 1
done

