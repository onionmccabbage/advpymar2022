import unittest
# we need to import the module to be tested
from my_point import Point

# here is a class to test our 'Point' class
class testPoint(unittest.TestCase): # inherit from TestCase
    # set up before each test is run
    def setUp(self):
        # this will be run before each test
        self.point = Point(3, 5) # this makes sure each test is independent

    # here are the tests
    def testMoveByA(self):
        '''test the moveBy method correctly alters x and y'''
        self.point.moveBy(5, 2)
        self.assertEqual( self.point.display(), (8, 7) )
    def testMoveByB(self):
        '''test the moveBy method for negative changes'''
        self.point.moveBy(-5, -2)
        self.assertEqual( self.point.display(), (-2, 3) )
    def testMoveByC(self):
        '''test the moveBy method with a specific dy value (expect a default dx value)'''
        self.point.moveBy(dy=9)
        self.assertEqual( self.point.display(), (3, 14) )
    def testHypotA(self):
        '''derive the hypotenuse'''
        self.point.moveBy(0, -1)
        r = self.point.hypot()
        self.assertEqual(r, 5.00)
    def testHypotB(self):
        '''derive the hypotenuse for awkward values'''
        r = self.point.hypot()
        self.assertAlmostEqual(r, 5.83, places=2) # 5.830951894845301
    def testExceptionRaised(self):
        '''if x or y are non-integer, we expect a TypeError'''
        with self.assertRaises(TypeError):
            Point('3', 4) # string where we expect an int
    def testPointCounter(self):
        '''test we can accurately count the number of point instances'''
        self.assertGreater(Point.points, 1) # how many points?


if __name__ == '__main__':
    unittest.main() # this will invoke our tests - runs anything starting with 'test'

