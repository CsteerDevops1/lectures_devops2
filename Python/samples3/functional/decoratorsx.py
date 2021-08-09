#!/usr/bin/env python3

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
 
def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped
 
#@makebold
#@makeitalic


def hello():
    greeting = "hello habr"
    result_string = "<b><i>" + greeting + "</i></b>"
    return result_string
 
print(hello())

def bye():
    greeting = "Good bye habr"
    result_string = "<i><b>" + greeting + "</b></i>"
    return result_string

print(bye())


