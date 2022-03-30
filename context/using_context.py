# Python 3 has a context manager
import sys
from contextlib import contextmanager

@contextmanager # make this function able to manage contexts
def stdout_redirect(new_stdout):
    save_stdout = sys.stdout # remember what the output is currently
    sys.stdout = new_stdout  # set a new output
    yield # this will yield the next available object to be written to the output
    sys.stdout = save_stdout # return the output to the original

if __name__ == '__main__':
    with open('mylog.txt', 'a') as fobj:
        with stdout_redirect(fobj):
            # we can write multiple lines
            print('''here is some output we need to capture
there are several lines
each redirected in turn
by our decorated function''')
            print('this also gets yielded')
    print('back to the normal terminal')