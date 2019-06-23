# add any imports here
import UsingVariables as uv
import UsingCollections as uc
import OtherTypes as ot
import UsingFunctions as uf
from UsingClasses import Stack, Person, DoctorPerson
import CollectionsChallenge as cc
import OtherTypesChallenge as otc
import datetime


def main():
      # cc.CreateListsAndShowThem()
      # cc.CreateTupleAndShowIt()
      # cc.CreateSetAndShow()
      # cc.EnglishSpanishNumerTranslations()
      # cc.FavoriteFruits()
      # otc.ShowSomeDates()
      # dob = datetime.datetime(1963,6,9)
      # print (f"age is {otc.GetAge(dob)}")

      # print(f"Divide 5/0: {otc.DivideTest(5, 0)}")
      # print(f"Divide 5/4: {otc.DivideTest(5, 4)}")

      # print(f"Lookup yves returns: {cc.ReturnStringFromCode('yves')}")

      # items = list(range(1, 25))
      # cc.ShowEveryThirdElement(items)

#     uv.DeclaringVariables()
#     uv.Comparisons()
#     ot.TryDateTime()
#     ot.TryArray()
#     ot.TryEnum()

#     uf.TryIf()
      print ("Calling: uf.MyFuncWithParams('SHOWIT', True)")
      uf.MyFuncWithParams("SHOWIT", True)
      print ("Calling: uf.MyFuncWithParams('showint')")
      uf.MyFuncWithParams("showit")
      print ("Calling: uf.MyFuncWithParamsAndReturn('showit', False)")
      result = uf.MyFuncWithParamsAndReturn("showit", False)
      print(f"result = {result}")

#     myStack = Stack()
#     myStack.push(4)
#     myStack.push(5)
#     print(f"myStack: {myStack}")
#     print(f"peek myStack: {myStack.peek()}")
#     print(f"pop myStack: {myStack.pop()}")
#     myStack.items = [10, 9, 8]
#     print(f"myStack: {myStack}")
#     print(f"peek myStack: {myStack.peek()}")
#     print(f"pop myStack: {myStack.pop()}")

#     print("\nAttempting polymorphism")
#     person = Person("John", "Doe")
#     doctor = DoctorPerson("Jane", "Doe")
#     print (f"Person: {person.FullName} says '{person.SaySomething()}'")
#     print (f"Doctor: {doctor.FullName} says '{doctor.SaySomething()}'")

# End of main

main()