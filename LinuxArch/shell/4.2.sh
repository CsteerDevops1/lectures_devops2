#!/bin/bash

cat /etc/passwd | cut -d: -f7 | sort | uniq -c


