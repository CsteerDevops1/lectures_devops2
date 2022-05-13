#!/bin/bash


a=1

while :
do
  (( a++ ))
  echo $a
  if [[ $a = 10 ]]
  then
    break
  fi
done
