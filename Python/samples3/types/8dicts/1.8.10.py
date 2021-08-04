#!/usr/bin/python3
"""
Составные типы данных
"""

mel = {
    "name": "Mark",
    "jobs": [
        "trainer",
        "writer",
    ],
    "web":  "www.rmi.net/~lutz",
    "home": {
        "state": "CO",
        "zip": 80501,
    },
}

print(mel["name"])

print(mel["jobs"])

print(mel["jobs"][1])

print(mel["home"]["zip"])
