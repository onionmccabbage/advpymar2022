# ways to pass arguments in Python
# we can always pass in sys.argv as parameters whwene we call the python module

def fnA(*args): # *args is all the positional arguments
    print(args) # args is ALWAYS a tuple of passed-in positional parameters

def fnB(**kwargs): # *kwargs is all the keyword arguments 
    print(kwargs) # kwargs is AWLAYS a dictionary of the positional arguments

def fnC(*args, **kwargs):
    print(args, kwargs)

if __name__ == '__main__':
    fnA(1, True, [], {}, (1,2,3))
    fnB( o={}, b=True, n=1, l=[], t=(1,2,3) )
    fnC(1, True, [], o={}, l=[], t=(1,2,3))