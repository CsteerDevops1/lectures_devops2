#!/usr/bin/env python3
"""
Копирование дерева каталогов
"""
from shutil import copytree


def _ignore(path, names):
    return []   # nothing will be ignored


source = "."
destination = "example"
copytree(source, destination, ignore=_ignore, dirs_exist_ok=True)
