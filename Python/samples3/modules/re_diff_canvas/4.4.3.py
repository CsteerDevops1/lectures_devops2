#!/usr/bin/env python3
"""
Регулярные выражения, подстановка
"""

import re

phone = "2004-959-559 #This is Phone Number"
print(phone)

# Delete Python-style comments
num = re.sub(r"#.*$", "", phone)
print("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r"\D", "", phone)
print("Phone Num : ", num)
