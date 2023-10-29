import os
import sqlalchemy

USERS = [
    {
        'first_name': 'Ugochukwu',
        'last_name': 'Okorocha',
        'email': 'ugochukwu1234@gmail.com'   
    },
    {
        'first_name': 'Favour',
        'last_name': 'Okoro',
        'email': 'favour1234@gmail.com'   
    },
    {
        'first_name': 'Chinaenye',
        'last_name': 'Okoro',
        'email': 'chinaenye1234@gmail.com'   
    },
    {
        'first_name': 'Uzoma',
        'last_name': 'Okoro',
        'email': 'Uzoma1234@gmail.com'   
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

metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table(
    "Users", 
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String)
)

metadata.create_all(engine)

with engine.connect() as conn:
    conn.execute(sqlalchemy.insert(users_table).values(USERS)
    )

    result =  conn.execute(sqlalchemy.select(users_table))
    
    for data in result:
        print(data)
        
    conn.commit()