import sqlite3

def writeDB():
    conn = sqlite3.connect('my_db') # connect or create if not exists
    # we need a cursor to interact with the database
    curs = conn.cursor()
    # next we structure the tables in this database
    # an SQL statement to insert values into the database (SQL uses DOUBLE QUOTES)
    # we should parameterize the values being inserted
    st = '''
    INSERT INTO zoo
    VALUES ("Penguin",265, 0.82)
    '''
    # execute the sql statement
    try:
        curs.execute(st)
        conn.commit() # without this, the datbase exchanges will not persist
    except Exception as e:
        print('There was a problem: {}'.format(e))
    finally:
        conn.close() # always a good idea to tidy up

if __name__ == '__main__':
    writeDB()