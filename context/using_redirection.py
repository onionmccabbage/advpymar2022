# we may wish to send output to something other than the default console
# e.g. to a log file print('data' file=fout)
# or a database, to another python module, to a stream, to an API ....

import sys # the default streams are sys.stdout and sys.stdin

class Redirect: # Python defaults to (object)
    '''
    Provide an easy way to redirect the standard output
    (instead of default console, send to a file etc.)
    '''
    def __init__(self, new_stdout): # we can pass ANYTHING to this fucntion
        self.new_stdout = new_stdout
    def __enter__(self): # override the built-in __enter__ method, (used by print etc.)
        '''Implement a redirect for output'''
        self.orig_stdout = sys.stdout # make a note of the current stdout output
        sys.stdout = self.new_stdout  # now sys.stdout has been redirected
    def __exit__(self, exc_type, exc_value, exc_traceback):
        '''restore the original stdout output'''
        sys.stdout = self.orig_stdout # the original sys.stdout has been restored

if __name__ == '__main__':
    print('Currently stdout is {}'.format(sys.stdout))
    with open('mylog.txt', 'a') as fobj:
        with Redirect(fobj):
            print('this gets written to our log file')
    print('normal output has been restored')