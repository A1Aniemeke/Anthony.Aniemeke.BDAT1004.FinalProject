#Installing necessary libraries
pip install pandas sqlalchemy psycopg2
pip install pandas sqlalchemy pyodbc flask google-charts


# Database connection details
from sqlalchemy import create_engine

server = 'bdat1004-group4.database.windows.net'
database = 'bdat1004group4'
username = 'bdat1004-group4'
password = 'Programming4$'
connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

# SQLAlchemy engine
engine = create_engine(connection_string)

print("Connected to the database!")



#Data loading to the Database
import pandas as pd
from sqlalchemy import create_engine
import time

# Database connection details
connection_string = "mssql+pyodbc://bdat1004-group4:Programming4$@bdat1004-group4.database.windows.net/bdat1004group4?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(connection_string)

def update_database():
    # Fetch updated data
    url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"
    data = pd.read_csv(url, sep='|')

    # Load data into the database
    data.to_sql('users', con=engine, if_exists='replace', index=False)
    print("Database updated successfully!")

# Simulating a 24-hour batch process
while True:
    update_database()
    time.sleep(24 * 60 * 60)  # Sleep for 24 hours

