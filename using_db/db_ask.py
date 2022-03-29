import sqlite3

def readDB():
    conn = sqlite3.connect('my_db') # connect or create if not exists
    curs = conn.cursor()
    st = '''
    SELECT creature, cost, count FROM zoo
    '''
    try:
        curs.execute(st)
        #now we can use our cursor to fetch data
        rows = curs.fetchall() 
    except Exception as e:
        print('There was a problem: {}'.format(e))
    finally:
        conn.close()
    # explore the returned rows
    print(rows) # a list of tuples for each data row

if __name__ == '__main__':
    readDB()