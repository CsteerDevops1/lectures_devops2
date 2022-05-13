#!/bin/bash


true  && echo True || echo False
false && echo True || echo False

for a in {1..3}
do
  if [ $a -eq 1 ]
  then
    echo a is equal to 1
  elif [ $a -eq 2 ]
  then
    echo a is equal to 2
  else
    echo a is not equal to 1 and 2
  fi
done
