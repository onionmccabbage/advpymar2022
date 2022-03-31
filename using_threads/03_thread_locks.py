# in most Pythpns there is a Global Interpreter Lock (GIL)
# This degrades performance
# we can take control of locks ourselves
from threading import Lock
import time
import random
import sys

def main():
    lock = Lock() # create an instanceo of the Lock class
    # lock.acquire()
    # try:
    #     for i in range(1,50):
    #         time.sleep(random.random()*0.1)
    #         sys.stdout.write('{} '.format(i))
    # except Exception as err:
    #     print(err)
    # finally:
    #     lock.release() # make sure the lock is released
    # alternative syntax
    with lock: # this will aquire the lock for us. NB locks are re-cycled - if accesed again, Python will manage locks efficiently
        for i in range(1,50):
            time.sleep(random.random()*0.1)
            sys.stdout.write('{} '.format(i))
    # no need to release the lock, since it is released when the with stament terminates

if __name__ == '__main__':
    main()