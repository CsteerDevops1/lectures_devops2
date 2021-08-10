#!/usr/bin/env python3
"""
Имена элементов и атрибутов
"""
import xml.dom.minidom

with open("example.xml", "r") as fh:
    dom = xml.dom.minidom.parse(fh)
    for node in dom.getElementsByTagName("device"):
        print(node.getAttribute("name"))
        for subnode in node.getElementsByTagName("port"):
            print(subnode.getAttribute("id"))
