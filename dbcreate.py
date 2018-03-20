import sqlite3 as db

conn = db.connect('test.db')
cursor = conn.cursor()
cursor.execute("Create table musics(title text,year text,singer text)")
print("table created")



