import sqlite3

DB = """movies.db"""

SELECT_MOVIES = """SELECT * FROM Movies WHERE year=?"""

FILTER = (1976,)

connection = sqlite3.connect(DB)

cursor = connection.cursor()

# Constructing a full string for the query, makes your application vulnerable to SQL injection attacks
cursor.execute(SELECT_MOVIES, FILTER)

print(cursor.fetchall())

connection.commit()
connection.close()
