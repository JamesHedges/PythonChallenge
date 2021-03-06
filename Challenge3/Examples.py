from People import Person, DoctorPerson, StudentPerson
from MyStack import MyStack


def DoStackOps():
    print("\n*** Stack Ops")
    myStack = MyStack()
    print("\n\tPushing 1,2,3 on the stack")
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)

    print ("\t\t MyStack:",myStack)

    print("\tPoping the stack")
    print ("\t\tPopped value:", myStack.pop())
    print ("\t\tStack now has:", myStack)

    myStack = MyStack(['a', 'b', 'c', 'd'])
    print (f"\n\tmyStack using initializer: \n\t\t{myStack}")

def FuncWithArgs(message, *args, **kwargs):
    print(f"message: {message}")
    for arg in args:
        print(f"\targ: {arg}")

    for key in kwargs:
        print(f"\tkwarg[{key}]: {kwargs[key]}")

def DoPolymorphism():
    print("\n*** Polymorphism")
    myPeople = list()
    myPeople.append(Person("\tTest", "Person"))
    myPeople.append(DoctorPerson("\tTest", "Doctor"))
    myPeople.append(StudentPerson("\tTest", "Student"))
    ShowMyPeople(myPeople)

    print("\n\tChange the first names...")
    myPeople[0].FirstName = 'George'
    myPeople[1].FirstName = 'Paul'
    myPeople[2].FirstName = "John"
    ShowMyPeople(myPeople)

def ShowMyPeople(myPeople):
    print("\tShowing myPeople...")
    for myPerson in myPeople:
        print ("\n\t\tmyPerson:", myPerson)
        print (f"\t\trepr: {myPerson}")
        print ("\t\tmyPerson says: ", myPerson.SaySomething())

def Main():
    DoStackOps()
    DoPolymorphism()
    FuncWithArgs("Test 1")
    FuncWithArgs("Test 2",'a', 1, 2.22)
    FuncWithArgs("Test 3", name="test", age='33')
    FuncWithArgs("Test 4", 'all', 100, 99.99, name="Tester", age='33')


Main()