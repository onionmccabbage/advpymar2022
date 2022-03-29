# we can write a custom generator
# use the 'yield' statement to make a generator
# here we generate 'byte' values
def byteGen(start, stop_before):
    s = start
    while s < stop_before:
        yield bytes(s) # the 'yield' statements makes this into a generator
        s+=1

if __name__ == '__main__':
    # we need an instance of our generator
    g = byteGen(70, 88)
    # iterate over our generator
    for b in g:
        print(b)
    print(g) # a generator!!
    # print(g.__next__()) # nope - it's exhausted