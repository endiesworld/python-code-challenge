import sqlite3

DB = """movies.db"""

MOVIES = [(2, 'Things Fall Apart', 'Acheber', 1989),
          (3, 'Blame the gods', 'Yinka', 1992),
          (4, 'Water an Enemy', 'Fola', 1996)]

INSERT_MOVIES = """ INSERT INTO Movies Values(?,?,?, ?)"""
SELECT_MOVIES = """SELECT * FROM Movies"""

connection = sqlite3.connect(DB)

cursor = connection.cursor()
cursor.executemany(INSERT_MOVIES, MOVIES)
cursor.execute(SELECT_MOVIES)

print(cursor.fetchall())

connection.commit()
connection.close()
