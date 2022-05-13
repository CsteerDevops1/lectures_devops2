#!/bin/bash
#https://www.linuxjournal.com/content/bash-trap-command

ctrlc_count=0

function no_ctrlc()
{
    let ctrlc_count++
    echo
    if [[ $ctrlc_count == 1 ]]; then
        echo "Stop that."
    elif [[ $ctrlc_count == 2 ]]; then
        echo "Once more and I quit."
    else
        echo "That's it.  I quit."
        exit
    fi
}

trap no_ctrlc SIGINT

while true
do
    echo Sleeping
    sleep 10
done

