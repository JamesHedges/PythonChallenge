def TryIf():
        x = 2
        if x == 2:
            x += 1
        elif x == 3:
            x -= 1
        else:
            x = 5
        print(x)

def MyFuncWithParams(name, isUpper = False):
    #test = str()
    if isUpper:
        test = name.lower()
    else:
        test = name.upper()
    
    print (f"test: {test}")


def MyFuncWithParamsAndReturn(name, isUpper = False):
    if isUpper:
        test = name
    else:
        test = name.upper()
    print ("test:", test)
    return "DONE"
