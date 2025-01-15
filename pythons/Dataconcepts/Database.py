import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER, name TEXT)')
cursor.execute("INSERT INTO users VALUES (1, 'Alice')")
conn.commit()
conn.close()


# Query
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
conn.close()


# sqlalchemy ORM for interacting with relational databases.
from sqlalchemy import create_engine,Column,Integer,String,MetaData, Table
engine = create_engine('sqlite:///example.db')
metadata = MetaData()
users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
)
metadata.create_all(engine)

# psycopy2 
import psycopg2
conn = psycopg2.connect(
    dbname="test_db",
    user="postgres",
    password="password",
    host="localhost"
)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(100))')
conn.commit()
conn.close()
