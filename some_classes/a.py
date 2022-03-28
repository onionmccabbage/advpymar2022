# we can use the Abstract Base Class (ABC)
from abc import ABCMeta, abstractmethod, abstractproperty

# here is an abstract BASE class
class AbstractShape():
    __metaclass_ = ABCMeta # ..from the abc imports
    @abstractmethod
    def __str__(self):
        pass
    @property
    @abstractmethod
    def name():
        pass # no body to the method

# here is an abstract class
class Shape(AbstractShape): # our class implements our Abstract Base Class
    def __init__(self, n, sides):
        self.name=n
        self.sides = sides # NB this is a directly accessible property
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, n):
        self.__name = n
    def __str__(self):
        return 'This shape is called {} with {} sides'.format(self.name, self.sides)