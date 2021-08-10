#!/usr/bin/env python3
"""
Кодировка base64
"""

import base64
encoded = base64.b64encode(b"data to be encoded")

print(encoded)

data = base64.b64decode(encoded)
print(data)
