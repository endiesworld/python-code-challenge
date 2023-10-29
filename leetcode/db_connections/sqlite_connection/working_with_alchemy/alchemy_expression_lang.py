import os
from sqlalchemy import create_engine, MetaData, Table, Column, select, Text, Integer

# Get the current directory where the script is located
current_directory = os.path.dirname(__file__)
# Move to the parent directory
parent_directory = os.path.dirname(current_directory)
# Specify the relative path to your SQLite database file
database_filename = 'movies.db'  # Change to your database file name

# Combine the current directory and the relative path to create the full path
database_path = os.path.join(parent_directory, database_filename)
# print(f"database_path: {database_path}")
# # Create an SQLAlchemy engine to connect to the SQLite database


engine = create_engine(f'sqlite:///{database_path}', echo=True)

metadata = MetaData()

movies_table = Table(
    "Movies", 
    metadata,
    Column("id", Integer),
    Column("title", Text),
    Column("director", Text),
    Column("year", Integer)
)

metadata.create_all(engine)

with engine.connect() as conn:
    result = conn.execute(select(movies_table))
    for data in result:
        print(data)