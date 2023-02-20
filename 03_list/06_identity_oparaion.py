Firstlist = []
Secondlist = []
if Firstlist == Secondlist:
    print("Both are equal")
else:
    print("Both are not equal")

if Firstlist is Secondlist:
    print("Both variable are pointing the same object")
else :
    print("Both variable are not pointing the same object")

Thirdlist = Firstlist

if Thirdlist is Firstlist:
    print("Both are pointing the same object")
else :
    print("point both are not pointing to the same object")    