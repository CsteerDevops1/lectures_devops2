# -*- encoding: utf-8 -*-
"""
Поиск элемента
"""
from xml.dom.minidom import parse

dom = parse("example.xml")
for node in dom.getElementsByTagName('configuration'):
    print node.toxml()
