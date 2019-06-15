# PythonChallenge
WorldRemit Denver Python Challenge

## Challenge Two - Moving Beyond Basics
### More Data Types
1. Declaring Explicitly
1. Collections
    * List
        * Represent a list of objects
        * Create with [] or list()
            * `numberList = [1, 2, 3]`
            * `emptyList = list()`
        * Lists are mutable - can insert and remove items
        * Example:
            ```python
            def listTest():
                    myList = ["one", "two", "three" ]
                    print(myList, "is of type", type(myList))
                    printList(myList)
                    myList.append("four")
                    printList(myList)
                    myList.remove("two")
                    myList.append("Oh My!")
                    printList(myList)

            def printList(theList):
                    print("\nPrinting a", type(theList).__name__)
                    for thing in theList:
                            print("\t"+thing)
            ```
        * See the documentation for many more operations on lists: https://docs.python.org/3/library/stdtypes.html#list
    * Tuple
        * Sequence of items
        * Is immutable - can NOT add or remove items
        * Create using ()
        * Example:
            ```python
            def tupleTest():
                    myTuple = ("one", 2, 3.14)
                    print(myTuple)
                    print(myTuple[1])
            ```
        * Can also create from a list
            ```python
            myList = ['one', 'two', 'three']
            myTuple = tuple(myList)
            ```
        * Why use tuples?
            * Use less space
            * Cannot accidentally alter them
            * Can use as dictionary keys
            * Can pack function args / returns
    * Range
        * Immutable sequence of numbers
        * Create with 
            * First n numbers: `myRange = range(10)` -->  returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            * Numbers start to stop: `myRange = range(2,5)` --> returns [2, 3, 4, 5]
            * Numbers start to stop by an increment: `myRange = range(1, 9, 2)` --> returns [1, 3, 5, 7, 9]
    * Set
        * Unordered set of unique objects
        * Can perform set operations like intersection, union, and difference
        * Create with () or set()
            * `mySet = ("one", "two", "three")`
            * `mySet = set()`
        * Can add and remove members
        * Example:
            ```python
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
            ```
        * Many more operations, see: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
    * Frozen Set
        * Same as set except it is immutable
    * Dictionary
        * Maps objects to a key
        * The key must be unique
        * Declare two ways:
            * With constructor: `myDict = dict(key1 = value1, key2 = value2, ... keyn = valuen)`
            * With initializer: `myDict = { key1: value1, key2: value2, ... keyn: valuen }`
        * Can get a value by index: `myDict["one"]`
            * Note the key "one" must exist in the dicrionary or the get will generate an exception. You can test with `myDict.contains(key)`
        * Can set a value by index: `myDict["one"] = "uno"`
        * Example: 
            ```python
            def dictionaryTest():
                    myDict = {"one": "uno", "two": "dos", "three": "tres"} 
                    printDictionary(myDict) 

                    myDict["four"] = "quatro"
                    printDictionary(myDict)

                    myDict.pop("three")
                    printDictionary(myDict)

                    myDict["two"] = "2"
                    printDictionary(myDict)
            ```
        * To see all dictionary operations: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
1. Other Built In Types
    * Date Time
        * Must import datetime module
        * Date - Naive (cannot locate) date
        * Time - Idealized (can locate (tz)) time
        * DateTime - Idealized (can locate) date and time
        * Time Delta
            ```python
            import datetime as dt

            def TryDateTime():
                print("\n*** Date Time Examples")
                myTime = dt.datetime(2019, 7, 1)
                print(f"Now: {dt.datetime.now()}")
                print(f"myTime: {myTime}")
            ```
    * Array - Efficient arrays of basic values (no objects)
        * Must import array module
        * Declare with a type
            * Signed int 'i'
            * Unsigned int 'I'
            * Float 'f'
            * Signed char 'b'
            * Unsigned char 'B'
            * Unicode char 'u'
        * Create explicitly: `myIntArray = array.array('i')`
        * Example:
            ```python
            from array import array

            def TryArray():
                print("\n*** Array Examples")
                
                myArray = array('I', [1,2,3])
                print(f"myArra[2] = {myArray[2]}")
                ShowArray(myArray)
                myArray.append(5)
                myArray.insert(3, 4)
                ShowArray(myArray)
            ```
    * Enum
        * Must import enum module
        * A set of symolic names
        * Example:
            ```python
            from enum import Enum

            class Color(Enum):
                Red = 1,
                Green = 2,
                Blue = 3

            def TryEnum():
                x = Color.Red
                print (f"Color.Red: {x.name}")

                if (x is Color.Red):
                    print(f"x has color red: {repr(x)}")
            ```
### Iterating
1. Can iterate over a collection that implements __itr__
1. Use for each loop `for x in myCollection:`
1. Example:
    ```python
    from array import array

    def ShowArray(showMe):
        print("[ ", end= '')
        for element in showMe:
            print(f"{element} ", end='')
        print("]")
    ```
### Truth Value Testing
1. Comparison Operators
    * Equal: ==
    * Not Equal: !=
    * Less Than: <
    * Less Than or Equal: <=
    * Greater Than: >
    * Greater Than or Equal: >=
    * Is Object Identity: is
    * Is Not Object Identity: is not
1. Boolean operators
    * And - x and y
    * Or - x or y
    * Not - not x
### Flow Control Statements
1. If Statement
    * Conditional execution when true
    * Syntax: if \<condition\>:
    * May optionally have an elif: / else:
    * Example:
        ```python
        x = 2
        if x == 2:
            x += 1
        elif x == 3:
            x -= 1
        else:
            x = 5
        print(x)
        ```
1. For Statement
    * See iterating above
1. While Statement
    * Used to repeat execution while an expression is true
    * Syntax
        ```python
        while expression:
            # do something
        
        ```
    * Can _break_ out of the loop
    * Can _continue_ to next iteration
    * Example:
        ```python
        notFound = True
        while notFound:
             if TimeIsUp():
                 continue          # do the next iteration
             if GettingTired()
                break              # done with the loop
             if LookForSomething():
                 notFound = False  # when something is found, end the loop
        ```
1. Try Except Statement  
    * Used to handle an error (exception)
    * Executes statements. If an exception is thrown, the error can be caught.
    * An optional block can be added to run at the end to do any necessary cleanup
    * Syntax:
        ```python
        try:
            # try some statement
        except Exception as ex:
            # handle the exception ex
        finally:
            # optionally do some cleanup
        ```
    * Example:
        ```python
        myInts = {1, 2, 3, 4}
        try:
            myInts[4] = 3
        except IndexError as ex:
            print (ex)
        ```
### More Functions
1. Parameters
    * Parameters are inputs to the function
    * Can have zero or more inputs
    * Prameters can have default values - from left to right
    * Example:
        ```python
        def MyFuncWithParams(name, isUpper = False):
            if isUpper:
                test = name
            else:
                test = name.upper()
            if test == 'SHOWIT'
                print (test)

        MyFunc("TEST NAME", isUpper=True)
        MyFunc("test name")
        ```
1. Return Values
    * Function may return a value using a return statement
    * Example:
        ```python
        def MyFuncWithParamsAndReturn(name, isUpper = False):
            if isUpper:
                test = name
            else:
                test = name.upper()
            if test == 'SHOWIT'
                print (test)
            
            return "DONE"

        MyFunc("TEST NAME", isUpper=True)
        MyFunc("test name")
        ```
1. See more on functions: https://www.w3schools.com/python/python_functions.asp
