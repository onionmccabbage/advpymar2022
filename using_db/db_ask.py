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
    # print(rows) # a list of tuples for each data row
    # iterate over the list to show each creature in a nice way
    for animal in rows:
        # using index numbers lets us say which value goes where, and repeat values.
        print('we have {2} (yes {2}) {0} costing {1:0.2f}'.format(animal[0], animal[1], animal[2]))

if __name__ == '__main__':
    readDB()