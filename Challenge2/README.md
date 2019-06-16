# PythonChallenge
WorldRemit Denver Python Challenge

## Challenge Two - Moving Beyond Basics
### More Data Types
1. Declaring Explicitly
    * Everything is an object
    * Any type can be declared explicityly, without an assignment
        * int: `myInt = int()`
        * float: `myFloat = float()`
        * string: `myString = str()`
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
        * Create with {} or set()
            * `mySet = {"one", "two", "three"}`
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
### Classes
1. Creating a class
    * Use the class keyword `class MyClass():` 
        - don't forget the colon!
    * Inherit another class by adding to parameters: `class MyClass(myBase):`
    * Example:
        ```python
        class MyClass():
            pass

        myCls = MyClass()
        ```
        - pass indicates there is no implementation
1. Constructor
    * Add a constructor with __init__ method
    * Include the self parameter
    * Add additional parameters - not required
    * Fields can be added and initialized
    * Example:
    ```python
    class Person():
        
        def __init__(self, fname, lname):
            self.fname = fname
            self.lname = lname
    ```
1. Methods
    * First parameter will be self
    * Example:
    ```python
    class Person():
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def FullName(self):
        return self.fname + " " + self.lname

    def SaySomething(self):
        return "We need to talk"
    ```

1. Properties
    * Use the @property decorator for the get
    * Use the @<property name>.setter decorator for the set (not required)
    * Field names can be 'mangled' to make the less accessable by starting with '__'
    * Example:
    ```python
    class Person():
    
    def __init__(self, fname, lname):
        self.__fname = fname
        self.__lname = lname

    @property
    def FirstName(self):
        return self.__fname

    @FirstName.setter
    def FirstName(self, fname):
        self.__fname = fname

    @property
    def FullName(self):
        return self.__fname + " " + self.__lname

    def SaySomething(self):
        return "We need to talk"
    ```
1. Inheritance
    * Inherit from a base class in declaration by adding to params: `class MyDerived(MyBase):`
    * Access the base class through super()
    * No constructor needs to be added, the base will be called
    * Example:
        ```python
            class DoctorPerson(Person):

                def SpecialName():
                    return "Dr. " + super().FirstName
        ```
1. Polymorphism
    * Polymorphism is achieve by overriding in derived class
    * Example:
        ```python
            class DoctorPerson(Person):

                def SaySomething(self):
                    return "The doctor says..."
        ```
1. Special Methods
    * Overloads language operators
    * Surrounded with double underscore
    * Most common and recommended is the to string method: `__str__(self)`
    * Special Methods for comparison

        <table>
            <tr>
                <td>__eq__(self, other)</td>
                <td>Equality</td>
                <td>self == other</td>
            </tr>
            <tr>
                <td>__ne__(self, other)</td>
                <td>Not Equal</td>
                <td>self != other</td>
            </tr>
            <tr>
                <td>__lt__(self, other)</td>
                <td>Less Than</td>
                <td>self < other</td>
            </tr>
            <tr>
                <td>__gt__(self, other)</td>
                <td>Greater Than</td>
                <td>self > other</td>
            </tr>
            <tr>
                <td>__le__(self, other)</td>
                <td>Less Than or Equal</td>
                <td>self <= other</td>
            </tr>
            <tr>
                <td>__ge__(self, other)</td>
                <td>Greater Than or Equal</td>
                <td>self >= other</td>
            </tr>
        </table>

        - Example:
            ```python
            class MyClass():
                def __init__(self):
                    self.Text1

                def __eq__(self, other)
                    return self.Text1 == other
            ```
    * Special Method for Math

        <table>
            <tr>
                <td>__add__(self, other)</td>
                <td>Add</td>
                <td>self + other</td>
            </tr>
            <tr>
                <td>__sub__(self, other)</td>
                <td>Subtract</td>
                <td>self - other</td>
            </tr>
            <tr>
                <td>__mul__(self, other)</td>
                <td>Multiply</td>
                <td>self * other</td>
            </tr>
            <tr>
                <td>__floordiv__(self, other)</td>
                <td>Floor Division</td>
                <td>self // other</td>
            </tr>
            <tr>
                <td>__truediv__(self, other)</td>
                <td>Division</td>
                <td>self / other</td>
            </tr>
            <tr>
                <td>__mod__(self, other)</td>
                <td>Modulus</td>
                <td>self % other</td>
            </tr>
            <tr>
                <td>__pow__(self, other)</td>
                <td>Power</td>
                <td>self ** other</td>
            </tr>
        </table>

        - Example (using add to concatination):
            ```python
            class MyClass():
                def __init__(self):
                    self.Text1

                def __add__(self, other):
                    return self.Text1 + " " + other
            ```
    * Other Common Special Methods

        <table>
            <tr>
                <td>__str__(self)</td>
                <td>To String</td>
                <td>str(self)</td>
            </tr>
            <tr>
                <td>__repr__(self)</td>
                <td>Echo Variable</td>
                <td>repr(self)</td>
            </tr>
            <tr>
                <td>__len__(self)</td>
                <td>Length</td>
                <td>len(self)</td>
            </tr>
        </table>

        - Example:
            ```python
            class MyClass():
                def __init__(self):
                    self.Text1

                def __str__(self):
                    return self.Text1
            ```
        