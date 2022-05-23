#!/bin/bash

a=1

for i in $(seq 1 100)
do
  echo $(( ++a ))
  if [[ $a = 11 ]]
  then
    break
  fi
done
