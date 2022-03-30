import socket
import sys

def myClient():
    # open a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # try to connect to our server
    param_t = ('localhost', 9874)
    sock.connect(param_t)
    # send a message to the server (from sys.argv)
    if len(sys.argv) > 1: # check if any arguments were passed in
        msg = ' '.join(sys.argv[1:]) # concaternate the arguments (using space between)
    else:
        msg = 'default message'
    sock.send( msg.encode() ) # all http MUST be encoded
    # handle any response from the server
    res = sock.recv(1024) # receive the first 1024 bytes
    print(res)
    # tidy up
    sock.close()

if __name__ == '__main__':
    myClient() # get our client up and running
