
class Stack():

    def __init__(self):
        self.__stackItems = list()

    def __str__(self):
        return self.__stackItems.__str__()

    @property
    def items(self):
        return self.__stackItems
    
    @items.setter
    def items(self, newItems):
        self.__stackItems = newItems
    
    def push(self, item):
        self.__stackItems.insert(0, item)
    
    def pop(self):
        return self.__stackItems.pop(0)

    def peek(self):
        return self.__stackItems[0]

    def clear(self):
        self.__stackItems.clear()

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
        pass
    
class DoctorPerson(Person):

    @property
    def FullName(self):
        return super().FullName + ", MD"

    def SaySomething(self):
        return "As a doctor..."
        
