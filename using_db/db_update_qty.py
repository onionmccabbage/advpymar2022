import sqlite3

def main():
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # ask the user which creatuee needs updating
    invalid = True
    while invalid:
        c = input('Which creature needs updating? ')
        if type(c)==str and len(c)>0: # we calidate in case the value was obtained from somewhere unsafe
            invalid = False
    # ask what te new quantity is
    q = int(float(input('How many? '))) # al input is string, so cast to an int
    # here is our SQL statement, with parameters
    st = '''
    UPDATE zoo
    SET count = {0}
    WHERE creature IS "{1}"
    '''.format(q, c)
    try:
        curs.execute(st)
        conn.commit()
    except Exception as err:
        print('Problem: {}'.format(err))
    finally:
        conn.close()

if __name__ == '__main__':
    main()