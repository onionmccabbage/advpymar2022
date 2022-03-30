# doctest lets us write tests as part of the doc string
import doctest

def nthPower(d, p):
    '''
    this function will return the nth power of a number
    we can ue doctest to write tests within the documentation like this:
    >>> nthPower(3, 2)
    9
    >>> nthPower(-3, 3)
    -27
    '''
    return d**p

def cubeIt(a, b):
    '''
    return the cube of all numbers from a to b
    >>> cubeIt(3, 9)
    [27, 64, 125, 216, 343, 512]
    >>> cubeIt(1, 11) # doctest:+ELLIPSIS
    [1, 8, ..., 1000]
    '''
    answers = []
    for i in range(a, b):
        answers.append(i**3)
    return answers

if __name__ == '__main__':
    # print(nthPower(3, 2)) # 9
    doctest.testmod(verbose=True)
    # print(cubeIt(3, 9))