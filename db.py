import sqlite3
#create a notes.sqlite database
con = sqlite3.connect("notes.sqlite")
#create a cursor to fetch from sql query
cur = con.cursor()
#define the table
sqlite_table = """ CREATE TABLE note (
    id integer PRIMARY KEY,
    content text NOT NULL
)"""
#create db
cur.execute(sqlite_table)
