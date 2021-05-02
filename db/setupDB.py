import sqlite3
import json
from pathlib import Path

with open('./db/config.json') as json_file:
    data = json.load(json_file)

databaseFile = Path(data['DATABASE_NAME'])

if databaseFile.is_file():
    print("Database ppab6.db already exists.")
    con = sqlite3.connect('file:./db/ppab6.db?mode=rw', uri=True)
    cur = con.cursor()
    print("The database has the following row content: (if it is blank, the db is empty)")
    for row in cur.execute('''SELECT * FROM users'''):
        print(row)

    response = input("Do you want to delete the database and recreate it? (press Y or N): ")
    if response == "Y":
        print("Deleting the database ppab6.db......")
        databaseFile.unlink()
        
        print("Creating the db ppab6.db.....")
        con = sqlite3.connect('file:./db/ppab6.db?mode=rwc', uri=True)
        cur = con.cursor()
        cur.execute('''CREATE TABLE users (username VARCHAR, password_hash VARCHAR)''')
    else:
        print("Not touching the database and exiting...")
else:
    print("Creating the database ppab6.db")
    con = sqlite3.connect('file:./db/ppab6.db?mode=rwc', uri=True)
    cur = con.cursor()
    cur.execute('''CREATE TABLE users (username VARCHAR, password_hash VARCHAR)''')
