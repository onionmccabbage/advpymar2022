from threading import Thread, Lock
# here are some global values
lock = Lock()
count1 = 0
count2 = 0

class MyClass(): # here we have a callable class
    def __call__(self, name):
        global lock, count1, count2
        for i in range(0, 20): # let the GIL manage any shared memroy locking
            count1 += 1
            print('count1 is {}'.format(count1))
        # use a lock to manage count2
        lock.acquire() # manage the locks ourself
        for i in range(0, 20):
            count2 += 1
            print('count2 is {}'.format(count2))
        lock.release()

if __name__ == '__main__':
    m1 = MyClass()
    m2 = MyClass()
    t1 = Thread(target=m1, args=('t1',))
    t2 = Thread(target=m2, args=('t2',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(count1, count2)