# file input and file output (fifo)
# NB we may well need to encode complex structures before storing them in a file

def main():
    '''simply write some text out to a text file'''
    # NB this is a file access object, NOT the file itself
    fout = open('output.txt', 'a') # 'a' will create or append to the file
    # we can switch the context of the 'print' statement so it outputs to a file
    print('here is some text content', file=fout)
    # it is always a good idea to close our file access object
    fout.close()

if __name__ == '__main__':
    main()