#!/usr/bin/env python3
"""
Добавление узла
"""
from xml.dom.minidom import parse
dom = parse("example.xml")

device = dom.createElement("device")
description = dom.createElement("description")
type = dom.createElement("type")
txt = dom.createTextNode("server")
dom.childNodes[0].appendChild(device)
device.appendChild(description)
description.appendChild(type)
type.appendChild(txt)
print(dom.toxml())
