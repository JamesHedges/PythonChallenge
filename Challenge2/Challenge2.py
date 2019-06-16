# add any imports here
import UsingVariables as uv
import UsingCollections as uc
import OtherTypes as ot
import UsingFunctions as uf
from UsingClasses import Stack, Person, DoctorPerson


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

    myStack = Stack()
    myStack.push(4)
    myStack.push(5)
    print(f"myStack: {myStack}")
    print(f"peek myStack: {myStack.peek()}")
    print(f"pop myStack: {myStack.pop()}")
    myStack.items = [10, 9, 8]
    print(f"myStack: {myStack}")
    print(f"peek myStack: {myStack.peek()}")
    print(f"pop myStack: {myStack.pop()}")

    print("\nAttempting polymorphism")
    person = Person("John", "Doe")
    doctor = DoctorPerson("Jane", "Doe")
    print (f"Person: {person.FullName} says '{person.SaySomething()}'")
    print (f"Doctor: {doctor.FullName} says '{doctor.SaySomething()}'")
    

def Hello():
    print("\nHello Python!")


# End of main

main()