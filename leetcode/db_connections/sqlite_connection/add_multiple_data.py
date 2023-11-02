import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
    	if exc_type is not None:
            print(f'an error occurred: {exc_val}')

DB = """movies.db"""

MOVIES = [(9, 'Asharami synergy', 'Tonye Cole', 2003),
          (10, 'Ikeja Electric', 'Tope Shonubi', 2015),
          (11, 'ATT Ikeja', 'Adeyonyi Moroti', 2018)]

INSERT_MOVIES = """ INSERT INTO Movies Values(?,?,?, ?)"""
SELECT_MOVIES = """SELECT * FROM Movies"""


with Database(DB) as db:
    db.cursor.executemany(INSERT_MOVIES, MOVIES)
    db.connection.commit()
    db.cursor.execute(SELECT_MOVIES)

    print(db.cursor.fetchall())

    
   
