#!/bin/bash

declare

declare -i a=4
echo $a
a=5
echo $a
a="rr"
echo $a

declare -r b="bb"
echo $b
b="cc"
echo $b

declare -p a
declare -p b
