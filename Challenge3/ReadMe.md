# PythonChallenge
Denver Python Challenge

## Challenge Three - Gotta Have Class
### What is Object Oriented Programming?
* A programming paradigm based on a collection of objects that communicate through messaging. An object is a package of related data and methods. Objects are modeled as classes. These models are base on the following principles: encapsulation, inheritance, polymorphism.
    - Encapsulation - Data and behaviors are encapsulted by the model in order to hide the data (data hiding) and expose the behaviors that act upon the data through the messaging interface.
    - Inheritance - The ablitlity to pass data and behavior from a parent on to a decendent. The parent is referred to as the base class and th decendent the derived class.
    - Polymorphism - The ability of a related class to inherit some behaviors while modifying other behaviors based on its context. The base class is a generalization while the derived classes are generally more specific. Consider a shape. Can you draw a shape? A square is a shape, can you draw a square. A circle is a shape. Can you draw a circle?
### Classes
1. Defining a class
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
1. Creating a Class
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
1. Adding Behaviors to a Class
    * Methods
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

1. Adding Data to a Class
    * Properties
    * Getter - Use the @property decorator for the get
    * Setter - Use the @<property name>.setter decorator for the set (not required)
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
### Inheritance
* Inherit from a base class in declaration by adding to params: `class MyDerived(MyBase):`
* Access the base class through super()
* No constructor needs to be added, the base will be called
* Example:
    ```python
        class DoctorPerson(Person):

            def SpecialName():
                return "Dr. " + super().FirstName
    ```
### Polymorphism
* Polymorphism is achieve by overriding in derived class
* Example:
    ```python
        class DoctorPerson(Person):

            def SaySomething(self):
                return "The doctor says..."
    ```
## For You To Do
1. Classes
    * Constructor
    * Inheritance
    * Polymorphism
    * Special Methods
    * and more