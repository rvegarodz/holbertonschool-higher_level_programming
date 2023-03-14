#!/usr/bin/python3
'''Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa'''
# Module for Connecting To MySQL database
import MySQLdb
from sys import argv


def filter_states(argv):
    '''Function that connect and fetch data'''

    # Input Arguments
    i_username = argv[1]
    i_password = argv[2]
    i_db = argv[3]

    # Function for connecting to MySQL database
    database = (MySQLdb.connect
                (host="localhost",
                 port=3306,
                 user=i_username,
                 passwd=i_password,
                 db=i_db,
                 charset="utf8"))

    # Making Cursor Object For Query Execution
    db_cursor = database.cursor()

    # Executing Query
    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")

    # Fetching Data
    query_rows = db_cursor.fetchall()

    # Printing Result of Query
    for row in query_rows:
        print(row)

    # Closing Cursor Object Connection
    db_cursor.close()

    # Closing Database Connection
    database.close()


if __name__ == "__main__":
    filter_states(argv[1:])
