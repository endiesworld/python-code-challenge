import sqlite3

DB = """movies.db"""
INSERT_MOVIE = """ INSERT INTO Movies Values(1, 'Taxi Driver', 'Martin Scorsese', 1976)"""
SELECT_MOVIES = """SELECT * FROM Movies"""

connection = sqlite3.connect(DB)

cursor = connection.cursor()
cursor.execute(INSERT_MOVIE)
cursor.execute(SELECT_MOVIES)

print(cursor.fetchone())

connection.commit()
connection.close()
