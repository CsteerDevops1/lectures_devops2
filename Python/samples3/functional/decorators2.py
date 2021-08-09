#!/usr/bin/env python3

def makebold(fn):
    def wrapped(*args):
        return "<b>" + fn(*args) + "</b>"
    return wrapped
 
def makeitalic(fn):
    def wrapped(*args):
        return "<i>" + fn(*args) + "</i>"
    return wrapped
 
@makebold
@makeitalic
def hello(*args):
    args = [ str(i) for i in args ]
    return "hello " + "".join(args) + " habr"
 
print(hello(222))
print(hello(222,333))
