#!/usr/bin/python3
"""
Ввод из консоли
"""
number = eval(input("Enter a number between 1 and 10: "))
if number <= 10:
    if number >= 1:
        print("Great!")
    else:
        print("Wrong!")
else:
    print("Wrong!")
