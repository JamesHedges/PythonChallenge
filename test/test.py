myList = ["one", 2, "tres", 3.14]

# for item in myList:
#     print(item, sep="u", end=" ")

class testit():
    def __init__(self, number):
        self.number = number

    @property
    def MyNumber(self):
        return self.number

    @MyNumber.setter
    def MyNumber(self, number):
        self.number = number

myClass = testit(234)
print (myClass.MyNumber)
myClass.MyNumber = 55
print(myClass.MyNumber)