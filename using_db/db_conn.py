import sqlite3 # or ANY other sql database engine
# make a conection to this database
# DB2
# import DB2
# conn = DB2.connect(dsn='ibm-DB', uid='analyst', pwd='db2pwd')

# Sybase
# import Sybase
# conn = Sybase.connect('SYBASE', 'username', 'passwd', 'databasename')

# Oracle
# import cx_Oracle
# conn = cx_Oracle.connect('username', 'passwd', 'hostname:port/SID')
# conn2 = cx_Oracle.connect('username/passwd@hostname:portno/SID')
# dsn_tns = cx_Oracle.makedsn('hostname', portno, 'SID')
# conn3 = cx_Oracle.connect('username', 'passwd', dsn_tns)

# MySQL
# import MySQLdb
# conn = MySQLdb.connect(host = "hostname", user = "username",
# passwd = "password", db = "dbname")

# PySQLite
# from pysqlite2 import dbapi2 as sqlite
# conn = sqlite.connect("mydb", connectionproperties)

# ODBC
# import odbc
# conn = odbc. odbc("myDSN/username/password")

def accessDB():
    '''
    This database will manage Zoo creatures. Each has a count (int), a creature-name and a cost (float)
    The primary key will be 'creature' (varchar)
    '''
    conn = sqlite3.connect('my_db') # connect or create if not exists
    # we need a cursor to interact with the database
    curs = conn.cursor()
    # next we structure the tables in this database
    # first, an SQL statement (plain text)
    st = '''
    CREATE TABLE zoo
    (creature VARCHAR(32) PRIMARY KEY,
     count INT,
     cost FLOAT
    )
    '''
    curs.execute(st)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    accessDB()