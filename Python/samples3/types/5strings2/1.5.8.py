#!/usr/bin/python3
"""
Форматирование строк
src: https://realpython.com/python-string-formatting/
"""

errno = 44107522304
name = 'Alice'

# Old-style
print('Omg %s! We have a error 0x%x!' % (name, errno))
print('Omg %(name)s! We have a error 0x%(errno)x!' % {
    "name": name,
    "errno": errno,
})

# .format
print('Omg {}! We have a error 0x{:x}!'.format(name, errno))
print('Omg {name}! We have a error 0x{errno:x}!'.format(name=name, errno=errno))

# f-strings
print(f'Omg {name}! We have a error {errno:#x}!')
