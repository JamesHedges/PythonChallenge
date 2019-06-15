import datetime as dt
from array import array
from enum import Enum

def TryDateTime():
    print("\n*** Date Time Examples")
    myTime = dt.datetime(2019, 7, 1)
    print(f"Now: {dt.datetime.now()}")
    print(f"myTime: {myTime}")

def TryArray():
    print("\n*** Array Examples")
    
    myArray = array('I', [1,2,3])
    print(f"myArra[2] = {myArray[2]}")
    ShowArray(myArray)
    myArray.append(5)
    myArray.insert(3, 4)
    ShowArray(myArray)

class Color(Enum):
    Red = 1,
    Green = 2,
    Blue = 3

def TryEnum():
    x = Color.Red
    print (f"Color.Red: {x.name}")

    if (x is Color.Red):
        print(f"x has color red: {repr(x)}")





def ShowArray(showMe):
    print("[ ", end= '')
    for it in showMe:
        print(f"{it} ", end='')
    print("]")

