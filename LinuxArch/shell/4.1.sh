#!/bin/bash


find . -type f -exec chmod 644 {} \;
find . -type d -exec chmod 755 {} \;

find /path/to/location -type f -print0 | xargs -0 chmod 644
find /path/to/location -type d -print0 | xargs -0 chmod 755
