#!/usr/bin/python3
"""
Сравнение
"""

# read string and convert to integer
number1 = input("Please enter first integer: ")
number1 = int(number1)

number2 = input("Please enter second integer: ")
number2 = int(number2)

if number1 == number2:
    print("%d is equal to %d" % (number1, number2))

if number1 != number2:
    print("%d is not equal to %d" % (number1, number2))

if number1 < number2:
    print("%d is less than %d" % (number1, number2))

if number1 > number2:
    print("%d is greater than %d" % (number1, number2))

if number1 <= number2:
    print("%d is less than or equal to %d" % (number1, number2))

if number1 >= number2:
    print("%d is greater than or equal to %d" % (number1, number2))
