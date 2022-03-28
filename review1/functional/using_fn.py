# instead of class-based coding many solution use purely functional coding
# this often involves map, filter and reduce
from functools import reduce

# some simple functions
def square(x):
    return x*x

def add(x, y):
    return x+y

def isOdd(n):
    return n%2 !=0 # True or False if even or odd

if __name__ == '__main__':
    # we need a list of square nubmers in a range
    sq_l = list(map(square, range(1,6)))
    print(sq_l)
    # here we use the filter function
    odd_l = list( filter( isOdd, range(1,27) ))
    print(odd_l)
    # using 'reduce' - apply a function cumulatively to every member of a collection
    r = reduce( add, odd_l )  
    print(r)