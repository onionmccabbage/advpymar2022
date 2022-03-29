# writing bytes to a file

def doWrite():
    # generate some 'byte' data
    bdata = bytes(range(0,256)) # 256 byte-values (0-255)
    # persist the byte data into a byte file
    fout = open('bfile', 'wb') # 'w' will (over)write 'b' for bytes
    # fout.write(bdata)
    # we can choose to write 'chunks' to our file
    size   = len(bdata)
    offset = 0
    chunk  = 64
    while True:
        if offset > size:
            break
        fout.write(bdata[offset:offset+chunk]) # start:stop-before
        offset+=chunk
    fout.close()

if __name__ == '__main__':
    doWrite()
