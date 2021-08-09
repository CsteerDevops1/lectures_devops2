#!/usr/bin/env python3


import pathlib, subprocess

p = pathlib.Path('qwe.txt')
if p.exists():
    p.unlink()

with p.open('a') as f1:
    print('a' * 9999, file=f1)
    print('b' * 999, file=f1)
    # append to the same file from another process
    subprocess.call("echo ccc >> qwe.txt", shell=True)

with p.open() as f1:
    # we expect 11000
    print(f1.read().index('ccc'))
