import os
import sqlalchemy

USERS = [
    {
        'first_name': 'Emmanuel',
        'last_name': 'Okoro',
        'email': 'emmanuel1234@gmail.com'   
    },
    {
        'first_name': 'Adaobi',
        'last_name': 'Okoro',
        'email': 'adal1234@gmail.com'   
    },
    {
        'first_name': 'Chidubem',
        'last_name': 'Emmanuel',
        'email': 'chidubem1234@gmail.com'   
    },
    {
        'first_name': 'Sochikamuma',
        'last_name': 'Emmanuel',
        'email': 'sochikamuma1234@gmail.com'   
    },
    ]

# Get the current directory where the script is located
current_directory = os.path.dirname(__file__)
# Move to the parent directory
parent_directory = os.path.dirname(current_directory)
# Specify the relative path to your SQLite database file
database_filename = 'users.db'  # Change to your database file name

# Combine the current directory and the relative path to create the full path
database_path = os.path.join(parent_directory, database_filename)

# # Create an SQLAlchemy engine to connect to the SQLite database
engine = sqlalchemy.create_engine(f'sqlite:///{database_path}', echo=True)

with engine.connect() as conn:
    conn.execute(sqlalchemy.text("""CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, email TEXT)"""
        )
    )

    conn.execute(sqlalchemy.text("""INSERT INTO Users(first_name, last_name, email) 
                                VALUES (:first_name, :last_name, :email)"""), USERS
    )

    result =  conn.execute(sqlalchemy.text("""SELECT * FROM Users"""))
    
    for data in result:
        print(data)
        
    conn.commit()