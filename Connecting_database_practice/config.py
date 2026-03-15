import os
from dotenv import load_dotenv
import psycopg2

# Loading all the variables from the .env file, and now can access through os
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT","5432")

# Function to return connection to database and none if no connection!
def get_db_connection():
    try:
        connection = psycopg2.connect(host=DB_HOST,database=DB_NAME,user=DB_USER,password=DB_PASSWORD,port=DB_PORT)
        return connection
    except Exception as e:
        print("Error Connecting to the database: ",e)
        return None

