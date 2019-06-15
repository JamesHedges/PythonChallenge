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
    if isUpper:
        test = name
    else:
        test = name.upper()
    if test == 'SHOWIT':
        print (test)


def MyFuncWithParamsAndReturn(name, isUpper = False):
    if isUpper:
        test = name
    else:
        test = name.upper()
    if test == 'SHOWIT':
        print (test)
    return "DONE"
