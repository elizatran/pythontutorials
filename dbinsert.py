import sqlite3 as db

conn = db.connect('test.db')
cursor = conn.cursor()
cursor.execute('insert into musics values("Khoc","2015","Dong Nhi")')
cursor.execute('insert into musics values("Em gai mua","2017","Huong Tram")')
conn.close()
