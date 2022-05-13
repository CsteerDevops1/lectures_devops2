#!/bin/bash

for i in {1..9}
do
  echo $i
done

ls -1

for i in {1..9}
do
  touch ${i}.jpg
done

ls -1

for i in {1..9}
do
  mv ${i}.jpg ${i}.png
done

ls -1

for i in *.png
do
  mv $i ${i/png/jpg}
done

ls -1

echo *

rm -f *.jpg



while [[ $a -lt 5 ]]
do
  echo $a
  a=$[$a+1]
done


until [[ $a -lt 2 ]]
do
  echo $a
  a=$[$a-1]
done

