#!/usr/bin/python3
'''Script that lists all cities from the database hbtn_0e_4_usa'''
# Module for Connecting To MySQL database
import MySQLdb
import sys


def get_cities_states(argv):
    '''Function that connect and fetch data'''

    # Input Arguments
    i_username = sys.argv[1]
    i_password = sys.argv[2]
    i_db = sys.argv[3]

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
    q_select = "SELECT cities.id, cities.name, states.name FROM cities "
    q_join = "INNER JOIN states ON cities.state_id = states.id"
    query = q_select + q_join
    db_cursor.execute(query)

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
    get_cities_states(sys.argv[1:])
