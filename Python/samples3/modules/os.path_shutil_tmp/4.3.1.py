#!/usr/bin/env python3
"""
Пути к файлам и каталогам
"""
import os

for path in ["/one/two/three", "/one/two/three/", "/", ".", ""]:
    print(path, ":", os.path.split(path))
    print("basename:", os.path.basename(path))
    print("dirname:", os.path.dirname(path))


paths = [
    "/one/two/three/four",
    "/one/two/threefold",
    "/one/two/three/",
]

print(os.path.commonprefix(paths))

for parts in [
    ("one", "two", "three"),
    ("/", "one", "two", "three"),
    ("/one", "/two", "/three"),
]:
    print(parts, ":", os.path.join(*parts))

for path in [
    "one//two//three",
    "one/./two/./three",
    "one/../one/two/three",
]:
    print(path, ':', os.path.normpath(path))

for path in [
    ".",
    "..",
    "./one/two/three",
    "../one/two/three",
]:
    print(path, ":", os.path.abspath(path))

for file in [
    __file__,
    os.path.dirname(__file__),
    "/",
    "./broken_link",
]:
    print("File        :", file)
    print("Absolute    :", os.path.isabs(file))
    print("Is File?    :", os.path.isfile(file))
    print("Is Dir?     :", os.path.isdir(file))
    print("Is Link?    :", os.path.islink(file))
    print("Mountpoint? :", os.path.ismount(file))
    print("Exists?     :", os.path.exists(file))
    print("Link Exists?:", os.path.lexists(file))


print(os.getcwd())
print(os.path.abspath(""))
print(os.path.abspath(".ssh"))
print(os.path.abspath("/home/you/.ssh"))
print(os.path.abspath(".ssh/../foo/"))
