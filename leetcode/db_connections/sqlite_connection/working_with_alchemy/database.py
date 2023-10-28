
import os
import sqlalchemy

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
engine = sqlalchemy.create_engine(f'sqlite:///{database_path}', echo=True)

# You can now use the engine to interact with the database, e.g., execute SQL queries
with engine.connect() as connection:
    result = connection.execute(sqlalchemy.text('SELECT * FROM Movies'))
    for row in result:
        print(row)

