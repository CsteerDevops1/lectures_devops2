#!/bin/bash

echo "Please enter Username:"
read username

echo "Please enter password:"
read -s password

echo "https://$username:$password@www.server-with-basic-auth.net/"

read -s -p "password please:" pass

echo
echo
echo $pass
