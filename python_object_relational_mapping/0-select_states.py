import MySQLdb

database = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="password", db="hbtn_0e_0_usa", charset="utf8")

db_cursor = database.cursor()
db_cursor.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = db_cursor.fetchall()
for row in query_rows:
    print(row)
db_cursor.close()
database.close()