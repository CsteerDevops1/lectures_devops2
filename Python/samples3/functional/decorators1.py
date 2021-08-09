#!/usr/bin/env python3

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
 
def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def makegood(fn):
    def wrapped():
        return "<good>" + fn() + "</good>"
    return wrapped
 
@makebold
@makeitalic
def hello():
    return "hello habr"
 
print(hello())

@makegood
@makeitalic
@makebold
def bye():
    return "Good Bye habr"
 
print(bye())

