# there are many things built in to Python
# many of them are avaialble as 'intrinsics'

class TopLevel(object):
    def __init__(self):
        pass

class Derived(TopLevel):
    '''this class is derived from TopLevel
    it has its own __Str__ method
    '''
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'Derived Class instance'

if __name__ == '__main__': # this is intrinsic to the current module
    t = TopLevel()
    d = Derived()
    print(d) # call the __str__
    # explore some intrinsic members of our instances
    print('class name is {}'.format(Derived.__name__))
    print('class docstring is {}'.format(Derived.__doc__))
    print('class dictionary is {}'.format(Derived.__dict__))
    print('class bases are {}'.format(Derived.__bases__))