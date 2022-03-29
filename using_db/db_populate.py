import sqlite3

def main():
    '''
    Here we pass parameters to the database table for each new creature
    '''
    creatures_t = (
        {'creature':'Albatros', 'count':1,   'cost':120.99},
        {'creature':'Bear',     'count':5,   'cost':323.56},
        {'creature':'Carp',     'count':120, 'cost':87.00},
        {'creature':'Deer',     'count':121, 'cost':12.99},
        {'creature':'Elk',      'count':7,   'cost':73.47},
        )
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # iterate over the creatures tuple, using '?' as a placeholder in SQL statements
    st = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''
    for item in creatures_t:
        try:
            # we should check thje values being inserted are safe (avoid SQL injection attack)
            curs.execute(st, (item['creature'], item['count'], item['cost']) )
            conn.commit()
        except Exception as err:
            print('SQL insert problem: {}'.format(err))
    conn.close() # always make sure the connection is closed

if __name__ == '__main__':
    main()