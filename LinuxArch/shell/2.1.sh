#!/bin/bash


usage ()
{
  echo "Usage: `basename $0` [ -c N-M ] file"
}

while getopts :hc:d:f: arg
do
  case $arg in
    h)  usage ; exit 0 ;;
    c)  NUMBERS=$OPTARG ; TYPE="CHAR" ;;   # characters
    d)  DELIMETR=$OPTARG ;;                # delimetr
    f)  FIELDS=$OPTARG ; TYPE="FIELD" ;;   # fields numbers
  esac
done


echo Numbers: $NUMBERS
echo Delimeter: $DELIMETR
echo Fields: $FIELDS
echo Type: $TYPE


#./2.1.sh -h
#./2.1.sh -c3-4
#./2.1.sh -c3-4 -d:
#./2.1.sh -c3-4 -d-
#./2.1.sh -c3-4 -d- -f3
