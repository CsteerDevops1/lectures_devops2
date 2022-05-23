#!/bin/bash -x
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

trap "a=5" SIGTERM

echo $$

a=0

while true
do
    echo Sleeping
    sleep 2
    if [[ $a = 5 ]]
    then
      break
    fi
done

echo "Finished while loop"

trap "exit 43" SIGINT SIGTERM

until false
do
  echo "Sleeping in until loop"
  sleep 12
done
