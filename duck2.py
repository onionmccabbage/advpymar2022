class Duck(object): # here we explicitly descend from the object type
    '''
    This Duck class encapsulates a 'name' string through get/set methods
    '''
    # classes may have properties and methods of the class itself
    count = 0
    def how_many(self):
        return self.count
    def __init__(self, name_param):
        self.__name = name_param
        Duck.count += 1 # increment the count
    # we can use decorators to declare the getter and setter methods
    @property
    def name(self): # the getter
        return self.__name
    @name.setter
    def name(self, new_name): # the setter
        if (isinstance(new_name,str)):
            self.__name = new_name
    # we can override built-in methods
    def __str__(self):
        return 'This duck is called {}'.format(self.__name)

if __name__ == '__main__':
    d2 = Duck('Ada')
    d2.name = 'Beatrice'
    d3 = Duck('Erica')
    print(d2.name)
    print(d2) # this will use our __str__ method
    print(d2.how_many()) # or d3.count


