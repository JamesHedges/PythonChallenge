# add any imports here
import UsingVariables as uv
import UsingCollections as uc
import OtherTypes as ot
import UsingFunctions as uf

def main():
    Hello()
    uv.DeclaringVariables()
    uv.Comparisons()
    ot.TryDateTime()
    ot.TryArray()
    ot.TryEnum()

    uf.TryIf()
    uf.MyFuncWithParams("SHOWIT", True)
    uf.MyFuncWithParams("showit")
    result = uf.MyFuncWithParamsAndReturn("showit", True)
    print(f"result = {result}")

def Hello():
    print("\nHello Python!")


# End of main

main()