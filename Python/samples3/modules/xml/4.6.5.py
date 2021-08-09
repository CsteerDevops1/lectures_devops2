# -*- encoding: utf-8 -*-
"""
Имена элементов и атрибутов
"""
import xml.dom.minidom

fh = open("example.xml","r")
doc = xml.dom.minidom.parse(fh)
for node in dom.getElementsByTagName('device'):
    print node.getAttribute("name")
    for subnode in node.getElementsByTagName('port'):
         print subnode.getAttribute("id")
