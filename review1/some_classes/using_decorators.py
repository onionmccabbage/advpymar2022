# python uses the @ sign to indicate a 'decorator'
# here is our own custom 'decorator'
# we need to display all parameters passed in to a function
def show_args(func): # here we pass a function into our function
    def new_func(*args, **kwargs):
        print('Running function called {}'.format(func.__name__))
        print('Positional arguments are {}'.format(args))
        print('Keyword arguments are {}'.format(kwargs))
        return func(*args, **kwargs) # call the passed-in function!
    return new_func

# here is a simple function, decorated with our custom decorator
@show_args
def add_ints(a, b):
    '''  return the sum of two integer values '''
    if isinstance(a, int) and type(b)==int:
        # all good - add them together
        return a+b
    else:
        return 'fail'

# this code ONLY runs when THIS module is called DIRECTLY
# (this code does NOT run if this module is imported elsewhere)
if __name__ == '__main__':
    x, y = [1,2]
    # print(x,y)
    print(add_ints(x,y))
    print(add_ints(a=3,b=4))
    print(add_ints(6, b=y))
