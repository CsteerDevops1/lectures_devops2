#!/usr/bin/python3
"""
Приоритет операторов\
https://docs.python.org/3/reference/expressions.html#operator-precedence
"""

#--+----------------------------------+---------------------------------------+
#  | Operator                         |  Description                          |
#--+----------------------------------+---------------------------------------+
# (expressions...), [expressions...], | Binding or parenthesized expression,  |
# {key: value...}, {expressions...}   | list display, dictionary display,     |
#                                     | set display                           |
# x[index], x[index:index],           | Subscription, slicing,                |
# x(arguments...), x.attribute        | call, attribute reference             |
# await x                             | Await expression                      |
# **                                  | Exponentiation                        |
# +x, -x, ~x                          | Positive, negative, bitwise NOT       |
# *, @, /, //, %                      | Multiplication, matrix multiplication,|
#                                     | division, floor division, remainder 6 |
# +, -                                | Addition and subtraction              |
# <<, >>                              | Shifts                                |
# &                                   | Bitwise AND                           |
# ^                                   | Bitwise XOR                           |
# |                                   | Bitwise OR                            |
# in, not in, is, is not,             | Comparisons, including membership     |
# <, <=, >, >=, !=, ==                | tests and identity tests              |
# not x                               | Boolean NOT                           |
# and                                 | Boolean AND                           |
# or                                  | Boolean OR                            |
# if – else                           | Conditional expression                |
# lambda                              | Lambda expression                     |
# :=                                  | Assignment expression                 |
#--+----------------------------------+---------------------------------------+