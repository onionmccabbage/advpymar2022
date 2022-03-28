from a import Shape

class Circle(Shape): # this class inherits from 'Shape'
    def __init__(self, n):
        self.name = n

if __name__ == '__main__':
    c = Circle('claire')
    print( c.name )