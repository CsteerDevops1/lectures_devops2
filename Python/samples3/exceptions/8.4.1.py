try:
    raise NameError('HiThere')
except NameError as ne:
    print('An exception flew by!')
    print(ne)
    print(dir(ne))
    raise
