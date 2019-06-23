'''
+------------------------
|  Class: Person
+------------------------'''
class Person():

    def __init__(self, fname, lname):
        self.__fname = fname
        self.__lname = lname

    def __str__(self):
        return self.FullName
    
    def __repr__(self):
        typeName = type(self).__name__
        return f"'{typeName}(FirstName={self.FirstName}, LastName={self.LastName})'"

    @property
    def FirstName(self):
        return self.__fname
    
    @FirstName.setter
    def FirstName(self, fname):
        self.__fname = fname

    @property
    def LastName(self):
        return self.__lname
    
    @LastName.setter
    def LastName(self, fname):
        self.__lname = lname

    @property
    def FullName(self):
        return self.__fname + " " + self.__lname

    def SaySomething(self):
        pass
    
'''
+------------------------
|  Class: DoctorPerson
+------------------------'''
class DoctorPerson(Person):

    @property
    def FullName(self):
        return super().FullName + ", MD"

    def SaySomething(self):
        return "As a doctor..."

'''
+------------------------
|  Class: StudentPerson
+------------------------'''
class StudentPerson(Person):        

    def SaySomething(self):
        return "Just a student..."
