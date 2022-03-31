from threading import Thread
import time
from timeit import default_timer
import random
import sys

# here is a class which is 'runnable' as a thread
class MyClass(Thread):
    def __init__(self, name):
        Thread.__init__(self) # call the parent __init__
        self.name = name # could use get/set methods
    def doStuff(self):
        for i in range(1,50):
            time.sleep(random.random()*0.1) # average about 2.5 seconds to run this
            sys.stdout.write(self.name)
    def run(self): # override hte built-in 'run' of Thread
        # called when this thread starts
        self.doStuff()

class Other: # this is NOT a Thread
    # we COULD provide an __init__ here
    def __call__(self, name): # we can target any class that includes __call__ even if it is not a Thread
        for i in range(1,50):
            time.sleep(random.random()*0.1) # average about 2.5 seconds to run this
            sys.stdout.write(name)

if __name__ == '__main__':
    m1 = MyClass('m1') # instance of our runnable class
    m2 = MyClass('m2')
    m3 = MyClass('m3')
    m4 = MyClass('m4')
    o  = Other()
    m5 = Thread(target=o, args=('m5',)) # target our class (just like targeting a function)
    print('begin running threads....')
    s = default_timer()
    m1.start()
    m2.start()
    m3.start()
    m4.start()
    m5.start()
    # if we use 'join' then this mainthread will be blocked until the spawned threads (re)join
    m1.join()
    m2.join()
    m3.join()
    m4.join()
    m5.join()
    e = default_timer()
    print('\nExecution time was {}'.format(e-s))