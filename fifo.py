# file input and file output (fifo)
# NB we may well need to encode complex structures before storing them in a file

def main():
    '''simply write some text out to a text file'''
    # NB this is a file access object, NOT the file itself
    fout = open('output.txt', 'a') # 'a' will create or append to the file (defaults to 'text')
    # we can switch the context of the 'print' statement so it outputs to a file
    print('here is some text content', file=fout)
    # it is always a good idea to close our file access object
    print(fout)
    fout.close()

# read back from our file
def my_read():
    try:
        fin = open('output.txt', 'rt') # 'r' means read 't' means text (default)
        r = fin.read() # read the whole thing
        print(r)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print('some other error occurred: {}'.format(e))
    finally:
        if fin:
            fin.close()

def readByLines():
    try:
        with (open('output.txt', 'r')) as fin: # use the file access object until it is exhausted
            # l = fin.readline() # read one line
            # l += fin.readline() # read one line
            lines = fin.readlines() # read all lines
            print('lines: {}'.format(lines)) # we have a list of all the lines
            # NB the with operator will close the fin object when done
    except Exception as e:
        print(e)
    finally:
        pass

# we try to avoid poluting the global scope
if __name__ == '__main__':
    main()
    my_read()
    readByLines()