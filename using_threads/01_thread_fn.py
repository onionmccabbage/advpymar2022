# we can run many threads, but they all execute on the same processor
# this means all our threads share the same instance of Python
# threads are parallelism within a process

from threading import Thread # this provides a thread access object
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
    # invoke our functions as threads (ANY function can be pased to a thread)
    t1 = Thread(target=myFunc, args=('t1',)) # arguments are passed as a tuple
    t2 = Thread(target=myFunc, args=('t2',))
    t3 = Thread(target=myFunc, args=('t3',))
    t4 = Thread(target=myFunc, args=('t4',)) 
    # t5 = Thread(target=myFunc, args=('t4',)) 
    # t6 = Thread(target=myFunc, args=('t4',)) 
    # t7 = Thread(target=myFunc, args=('t4',)) 
    # t8 = Thread(target=myFunc, args=('t4',)) 
    # t9 = Thread(target=myFunc, args=('t4',)) 
    # t0 = Thread(target=myFunc, args=('t4',)) 
    # ta = Thread(target=myFunc, args=('t4',)) 
    # tb = Thread(target=myFunc, args=('t4',)) 
    # tc = Thread(target=myFunc, args=('t4',)) 
    # td = Thread(target=myFunc, args=('t4',)) 
    # te = Thread(target=myFunc, args=('t4',)) 
    # we start our threads
    t1.start() # begin to run the target function on a new thread
    t2.start()
    t3.start()
    t4.start()
    # t5.start()
    # t6.start()
    # t7.start()
    # t8.start()
    # t9.start()
    # t0.start()
    # ta.start()
    # tb.start()
    # tc.start()
    # td.start()
    # te.start()
    print('waiting for threads to (re)join\n')
    t1.join() # join will BLOCK this main thread until the other threads terminate
    t2.join()
    t3.join()
    t4.join()
    # t5.join()
    # t6.join()
    # t7.join()
    # t8.join()
    # t9.join()
    # t0.join()
    # ta.join()
    # tb.join()
    # tc.join()
    # td.join()
    # te.join()
    e = default_timer() # since we used 'join' this timer accurately tells how long all the threads took to complete
    print('\nTotal execution time was {}'.format(e-s))