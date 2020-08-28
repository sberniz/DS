import psycopg2
from os import getenv
import csv
"""" Comments Database Upload Script from csv """ 
#CONNCT
HEROKU_POSTGRESQL_WHITE_URL="DB_URL for login"
#COMMENT TABLE CREATION
COMMENTS = """CREATE TABLE IF NOT EXISTS comments ( 
    id SERIAL PRIMARY KEY NOT NULL,
    comment TEXT,
    story_title TEXT,
    compound FLOAT,
    subjectivity FLOAT,
    saltiness FLOAT,
    created_at TIMESTAMP,
    user_id INT);"""

##

# Connection to the database script... 
pg_conn = psycopg2.connect(HEROKU_POSTGRESQL_WHITE_URL)
pg_curs = pg_conn.cursor()
print(pg_conn)
pg_curs.execute("DROP TABLE IF EXISTS comments")
pg_conn.commit()
pg_curs.execute(COMMENTS)
pg_conn.commit()

# Script to read rows from csv, upload to created table on postgres sql
with open ('comm4.csv','r') as f:
    next(f)
    reader =csv.reader(f,delimiter='|')
    counter = 0
    for row in reader:
        query = """INSERT INTO comments (comment,story_title,compound,subjectivity,saltiness,created_at,user_id) VALUES ('{}','{}',{},{},{},'{}',{})""".format(str(row[1]),str(row[2]),row[3],row[4],row[5],row[6],row[7])

        print(query)
        pg_curs.execute(query)

pg_conn.commit()
pg_curs.close()
pg_conn.close()