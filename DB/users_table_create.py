# Database info 
import psycopg2
from os import getenv
"""Script to create user table and upload content """
#CONNCT
#HEROKU_POSTGRESQL_WHITE_URL = getenv('HEROKU_POSTGRESQL_WHITE_URL')
DATABASE_URL="credentials info"
pg_conn = psycopg2.connect(DATABASE_URL)
pg_curs = pg_conn.cursor()

# user table schema
USER = """CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY NOT NULL,
    username VARCHAR(300),
    saltiness FLOAT,
    salty_description VARCHAR(300));"""

# Functions to connect and execute DB queries
def db_connect(dbname='hn.sqlite3'):
        return sqlite3.connect(dbname)

def execute_query(cursor,query):
    cursor.execute(query)
    return cursor.fetchall()
# executing the queries below:
if __name__ == '__main__':
    conn = db_connect()
    curs = conn.cursor()
    q = "DROP TABLE IF EXISTS users"
    pg_curs.execute(q)

    pg_curs.execute(USER)

    with open('users_final.csv', 'r') as f:
        next(f) # Skip the header row.
        pg_curs.copy_from(f, 'users', sep=',',columns=('username','saltiness','salty_description'))
    

    pg_conn.commit()
    pg_curs.close()
    pg_conn.close()
