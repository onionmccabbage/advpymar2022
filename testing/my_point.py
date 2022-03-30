# here is a 'point' class, representing a point in x-y space
# also we will derive the hypotenue from x and y

class Point(object):
    '''
    Class representing x-y values in 2-d space wuit herived hypotenuse
    '''
    points = 0 # count how many Point instances are created
    def __init__(self, x, y):
        self.x = x # make use of the x setter method
        self.y = y
        Point.points += 1 # increment the count every time __init__ is called
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        if type(new_x)==int:
            self.__x = new_x
        else:
            raise TypeError
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        if type(new_y)==int:
            self.__y = new_y
        else:
            raise TypeError
    def hypot(self):
        '''derive the hypotenuse from x and y'''
        h = (self.x**2+self.y**2)**0.5
        return h
    def display(self): # return a tuple
        return (self.x, self.y)
    def moveBy(self, dx=0, dy=0):
        '''move the point by dx and dy'''
        self.x += dx
        self.y += dy

if __name__ == '__main__':
    p1 = Point(3,4)
    print( p1.display() )
    print( p1.hypot() )
    p2 = Point(-3, -4)
    p2.moveBy(6, 7)
    print( p2.display() )
    print(  Point(3,5).hypot() )