# -*- encoding: utf-8 -*-
"""
Добавление узла
"""
from xml.dom.minidom import parse
dom = parse("example.xml")

device = dom.createElement("device") 
description = dom.createElement("description")
type = dom.createElement("type")
txt = dom.createTextNode("server")
dom.childNodes[1].appendChild(device)
device.appendChild(description)
description.appendChild(type)
type.appendChild(txt)
print dom.toxml()
