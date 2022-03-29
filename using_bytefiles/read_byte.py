# reading from a byte file

def doRead():
    fin = open('bfile', 'rb') # 'read' 'bytes'
    bdata = fin.read()
    print(bdata)
    s = str(bdata)
    print(s)

if __name__ == '__main__':
    doRead()