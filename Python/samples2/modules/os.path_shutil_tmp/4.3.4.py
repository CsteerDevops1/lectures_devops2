# -*- encoding: utf-8 -*-
"""
Создание временных файлов
"""
import tempfile

# read input file
inputFile = open('input.txt', 'r')

# create temporary file
tempFile = tempfile.TemporaryFile()                   # we don't even need to 
first_process(input = inputFile, output = tempFile)   # know the filename...

# create final output file
outputFile = open('output.txt', 'w')
second_process(input = tempFile, output = outputFile)