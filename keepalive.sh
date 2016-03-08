#!/bin/bash
# to counter wandering parent process, use pgrep
# to ensure leda stays alive



while true
do
    pgrep main.py > $HOME/tmp/ledaLastPID.txt
    if [ $? -eq 1 ]
    then
        $HOME/project-leda/main.py > $HOME/tmp/leda.log &
        echo "Watchdog restarting LEDA at $(date)"
    fi
    sleep 1
done

