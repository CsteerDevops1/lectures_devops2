# -*- encoding: utf-8 -*-
"""
Переменные окружения
"""
import os

os.environ['USER'] = 'Mel'
os.popen('python echoenv.py').read()

import os
os.environ.keys()

os.environ['TEMP']

os.environ['TEMP'] = r'c:\temp'
os.environ['TEMP']