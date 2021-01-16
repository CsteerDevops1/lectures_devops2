# -*- encoding: utf-8 -*-
"""
Копирование дерева каталогов
"""
from shutil import copytree

def _ignore(path, names):
    return []   # nothing will be ignored

copytree(source, destination, ignore=_ignore)