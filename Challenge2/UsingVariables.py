def DeclaringVariables():
    myBool = bool()
    print(f"\nmyBool = {myBool} and is type {type(myBool).__name__}")

    myInt = int()
    print(f"\nmyInt = {myInt} and is type {type(myInt).__name__}")

    myFloat = float()
    print(f"\nmyFloat = {myFloat} and it type {type(myFloat).__name__}")

    myComplex = complex()
    print(f"\nmyComplex = {myComplex} and it type {type(myComplex).__name__}")

    print("\n")

def Comparisons():
    myInt1 = 10
    myInt2 = 999
    myInt3 = myInt2

    print(f"\nLess than: myInt1 ({myInt1}) < myInt2 ({myInt2}) is {myInt1 < myInt2}")
    print(f"Less than or equal: myInt2 ({myInt2}) <= myInt3 ({myInt3}) is {myInt2 <= myInt3}")
    print(f"Greater than: myInt2 ({myInt2}) > myInt1 ({myInt1}) is {myInt2 > myInt1}")
    print(f"Greater than or equal: myInt2 ({myInt2}) >= myInt3 ({myInt3}) is {myInt2 >= myInt3}")
    print(f"Equal to: myInt2 ({myInt2}) == myInt3 ({myInt3}) is {myInt2 == myInt3}")
    print(f"Not equal to: myInt1 ({myInt1}) != myInt2 ({myInt2}) is {myInt1 != myInt2}")
    print(f"Is object type: myInt2 is myInt3 is {myInt2 is myInt3}")
    print(f"Is not object: myInt1 is not myInt3 is {myInt1 is not myInt3}")
    print("\n")

