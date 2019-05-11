# add any imports here

def main():
        # print("\nHello Python!")
        # variablesTest()
        setTest()
        listTest()
        #dictionaryTest()
        #tupleTest()
        # showDrinks()

# End of main

def variablesTest():
        print("\nVariables Exploration")
        testBool = True
        testFloat = 123.456
        testInt = 12345678
        testString = "All good men come to the aid of their country"

        print("\ttest Bool:", testBool, "it's type is", type(testBool)) 
        print("\ttest Float:", testFloat, "it's type is", type(testFloat)) 
        print("\ttest Int:", testInt, "it's type is", type(testInt)) 
        print("\ttest String:", testString, "it's type is", type(testString)) 

        testBool2 = testBool
        testFloat2 = testFloat
        testInt2 = testInt
        testString2 = testString

        print("\ttest Bool 2:", testBool2, "it's type is", type(testBool2)) 
        print("\ttest Float 2:", testFloat2, "it's type is", type(testFloat2)) 
        print("\ttest Int 2:", testInt2, "it's type is", type(testInt2)) 
        print("\ttest String 2:", testString2, "it's type is", type(testString2)) 

 # End of variablesTest()   

def setTest():
        mySet = { "one", "two", "three" }
        print(mySet, "is of type", type(mySet))
        printList(mySet)
        mySet.add("four")
        printList(mySet)
        mySet.remove("two")
        mySet.add("Oh My!")
        printList(mySet)
        secondSet = { "uno", "dos", "tres" }
        printList(secondSet)

        # union
        unionSet = mySet.union(secondSet)
        printList(unionSet)

        mySet.add("two")
        secondSet.add("cinco")

        # intersction
        printList(unionSet.intersection(mySet))
        printList(unionSet.intersection(secondSet))

 # End of setTest 

def listTest():
        myList = ["one", "two", "three" ]
        print(myList, "is of type", type(myList))
        printList(myList)
        myList.append("four")
        printList(myList)
        myList.remove("two")
        myList.append("Oh My!")
        printList(myList)
        secondList = ["uno", "dos", "tres"]
        printList(secondList)

       
 # End of listTest 

def dictionaryTest():
        myDict = {"one": "uno", "two": "dos", "three": "tres"} 
        printDictionary(myDict) 

        myDict["four"] = "quatro"
        printDictionary(myDict)

        myDict.pop("three")
        printDictionary(myDict)

        myDict["two"] = "2"
        printDictionary(myDict)

# End of dictionaryTest

def tupleTest():
        myTuple = ("one", 2, 3.14)
        print(myTuple)
        print(myTuple[1])

# End of tupleTest

def printDictionary(theDict):
        print("\nPrinting a dictionary")
        for key, val in theDict.items():
                print("\tKey:", key, "Value:", val)

def printList(theList):
        print("\nPrinting a", type(theList).__name__)
        for thing in theList:
                print("\t"+thing)

# End of printList

def showDrinks():
        print("\nDictionary Exploration")
        drinks = {
        'martini': {'vodka', 'vermouth'}, 
        'black russian': {'vodka', 'kahlua'}, 
        'white russian': {'cream', 'kahlua', 'vodka'}, 
        'manhattan': {'rye', 'vermouth', 'bitters'}, 
        'screwdriver': {'orange juice', 'vodka'} 
        }

        print("\nCheck for vodka drinks:")
        for name, contents in drinks.items():
                if 'vodka' in contents:
                        print("\t" + name)

        print("\nCheck for vodka withou vermouth or cream")            
        for name, contents in drinks.items():
                if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
                        print("\t" + name)

# End of showDrinks

main()