#!/bin/bash


str="Hello world!"

echo $str

echo ${str/world/bash}

echo ${#str}

echo ${str+privet\ mir}

echo $str

echo ${str2=privet\ mir2}

echo $str2

echo ${str2:2:5}
