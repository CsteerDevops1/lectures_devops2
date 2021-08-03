#!/usr/bin/python3
"""
Объединение с форматированием
"""

list1 =  [ "A", "B", "C", "D", "E", "F" ]
string2 = "___"

print("List is:", list1)
print('Joining with "%s": %s' \
   % ( string2, string2.join ( list1 ) ))
print('Joining with "-.-":', "-.-".join( list1 ))
