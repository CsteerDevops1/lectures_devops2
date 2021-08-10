#!/usr/bin/env python3
"""
Создание временных файлов
"""
import tempfile

# read input file
input_file = open("input.txt", "r")

# create temporary file
temp_file = tempfile.TemporaryFile()
# we don't even need to know the filename...
first_process(input=input_file, output=temp_file)

# create final output file
output_file = open("output.txt", "w")
second_process(input=temp_file, output=output_file)
