#!/usr/bin/env python3
"""
Поиск элемента
"""
from xml.dom.minidom import parse

dom = parse("example.xml")
for node in dom.getElementsByTagName("name"):
    print(node.toxml())
