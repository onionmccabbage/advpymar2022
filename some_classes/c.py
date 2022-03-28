from a import Shape


# here is a concrete class
class Circle(Shape): # this class inherits from 'Shape'
    def __init__(self, n, sides):
        self.name = n # or we could call super
        self.sides = '1 or infinite, depending on your view'

class Square(Shape):
    def __init__(self, n, sides):
        # we can call methods in the parent class
        super().__init__(n, sides)
        # self.name = n

if __name__ == '__main__':
    c = Circle('claire', 1)
    s = Square('Reg', 4)
    print( c.name )


    print(s, c)
