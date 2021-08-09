#!/usr/bin/env python3
"""
Добавление элемента
"""
from xml.dom.minidom import parse

dom = parse("example.xml")
x = dom.createElement("device")  # creates <foo />
dom.childNodes[0].appendChild(x)  # appends at end of 1st child's children
print(dom.toxml())
