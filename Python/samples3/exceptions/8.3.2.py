class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        print(cls)
        raise cls()
    except B:
        print("caught B")
    except C:
        print("caught C")
    except D:
        print("caught D")

#for cls in [B, C, D]:
#    try:
#        raise cls()
#    except B:
#        print("B")
#    except C:
#        print("C")
#    except D:
#        print("D")
