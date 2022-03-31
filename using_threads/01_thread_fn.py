# we can run many threads, but they all execute on the same processor
# this means all our threads share the same instance of Python
# threads are parallelism within a process

from threading import Thread
import time
from timeit import default_timer
import random
import sys

# here is a function which we will run as a thread
def myFunc(name):
    for i in range(1,50):
        time.sleep(random.random()*0.1)
        sys.stdout.write(name)

if __name__ == '__main__':
    s = default_timer()
    # myFunc('a')
    # myFunc('b')
    # myFunc('c')
    # myFunc('d')
    # invoke our functions as threads
    t1 = Thread(target=myFunc, args=('t1',)) # arguments are passed as a tuple
    t2 = Thread(target=myFunc, args=('t2',))
    t3 = Thread(target=myFunc, args=('t3',))
    t4 = Thread(target=myFunc, args=('t4',)) 
    # # we start our threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    e = default_timer()
    print(e-s)