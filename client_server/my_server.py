import socket # lets us open a socket to listen for requests

def myServer():
    # the most common sockets are AF_INET and STREAM
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # we can construct a tuple of parameters
    param_t = ('localhost', 9874) # server and port
    server.bind( param_t ) # set our server parameters
    # begin listening for requests
    server.listen(4) # handle up to four requests
    print('The server is listening on port {} on {}'.format(param_t[1], param_t[0]))
    # here is a run-loop so we can continuosly respond to requests
    while True:
        # unpack any requests from clients
        (client, addr) = server.accept()
        print(client, addr)
        # read any data received from the client
        buf = client.recv(1024) # read the first 1024 bytes from the client request
        print('Server received {}'.format(buf))
        # decide what to do about this... here we will send the data back, CAPITALIZED
        resp = buf.upper()
        client.send(resp)
        # provide a way to quit the server - if the client sents 'quit'
        if buf == b'quit':
            server.close()
            break # break out of the while loop

if __name__ == '__main__':
    myServer() # get our server running!