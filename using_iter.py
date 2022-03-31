# iter is built in to python
l = [False, 7, 'text', (5,4,3)] # a list
l_iter = iter(l) # we now have an iterable list

print( l_iter.__next__() )
print( l_iter.__next__() )
print( l_iter.__next__() ) # could not do this with the original list

r = reversed(l) # reverse teh members of the list AND make it iterable
print( r.__next__() )