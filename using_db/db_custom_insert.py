import sqlite3

def writeDB():
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # ask the user for details to be added
    invalid = True
    while invalid:
        c = input('Creature Name: ')
        if type(c)==str and len(c)>0:
            invalid = False
    invalidCount = True
    while invalidCount:
        q = int( float( input( 'Quantity: ' ) ) ) # NB ALL input is always a string, so cast as a float then an int
        if q>-1:
            invalidCount = False
    p =input('Cost: ')
    st = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''
    try:
        curs.execute(st, (c, q, p)) # use our values for the placeholders in the sql statement
        conn.commit()
    except Exception as e:
        print('There was a problem: {}'.format(e))
    finally:
        conn.close()

if __name__ == '__main__':
    writeDB()