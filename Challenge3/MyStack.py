class MyStack():

    def __init__(self):
        self.__stackItems = list()

    def __str__(self):
        return self.__stackItems.__str__()

    def __repr__(self):
        return type(self).__name__

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

