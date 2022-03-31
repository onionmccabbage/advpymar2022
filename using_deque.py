# deque is a double-ended queue
# normal ordinal collections let us manage the 'end' members
# e.g. append() and pop()
# deque also has popleft and appendleft
from collections import deque

def pal(word): # a palindrome checker: tenet, racecar, madam etc.
    dq = deque(word) # deque can take any ordered collection
    while len(dq)>1:
        if dq.popleft() != dq.pop():
            return False # not a palindrome
    return True # we have a palindrome

if __name__ == '__main__':
    print( pal('tenet') )
    print( pal('racecar') )
    print( pal('halibut') ) # False
    print( pal('madamimadam') )