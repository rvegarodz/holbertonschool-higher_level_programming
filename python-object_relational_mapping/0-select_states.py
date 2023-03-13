#!/usr/bin/python3
'''Script that lists all states from the database hbtn_0e_0_usa'''

# Module for Connecting To MySQL database
import MySQLdb

# Function for connecting to MySQL database
database = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="password", db="hbtn_0e_0_usa", charset="utf8")

# Making Cursor Object For Query Execution
db_cursor = database.cursor()

# Executing Query
db_cursor.execute("SELECT * FROM states ORDER BY id ASC")

# Fetching Data
query_rows = db_cursor.fetchall()

# Printing Result of Query
for row in query_rows:
    print(row)

# Closing Cursor Object Connection
db_cursor.close()

# Closing Database Connection
database.close()