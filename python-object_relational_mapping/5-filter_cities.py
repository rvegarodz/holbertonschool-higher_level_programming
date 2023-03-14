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
    ui_name = {sys.argv[4]}

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
    q_select = "SELECT cities.name FROM cities "
    q_join = "INNER JOIN states ON cities.state_id = states.id "
    q_where = "WHERE states.name=%s"
    query = q_select + q_join + q_where
    db_cursor.execute(query, ui_name)

    # Fetching Data
    query_rows = db_cursor.fetchall()
    q_len = len(query_rows)
    i = 0

    # Printing Result of Query
    for row in query_rows:
        print(row[0], end="")
        if i < q_len - 1:
            print(", ", end="")
            i += 1
    print()

    # Closing Cursor Object Connection
    db_cursor.close()

    # Closing Database Connection
    database.close()


if __name__ == "__main__":
    get_cities_states(sys.argv[1:])
