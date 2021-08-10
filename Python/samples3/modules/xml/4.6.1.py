#!/usr/bin/env python3
"""
Разбор XML формата
"""
from xml.dom.minidom import parse, parseString

dom1 = parse("example.xml")   # parse an XML file
dom2 = parseString("<myxml>Some data <empty/> some more data</myxml>")
print(dom1.toxml())
print(dom2.toxml())
