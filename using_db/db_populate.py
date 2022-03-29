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

if __name__ == '__main__':
    main()