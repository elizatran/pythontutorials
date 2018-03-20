import sqlite3 as db

conn = db.connect('test.db')
cursor = conn.cursor()
cursor.execute("drop table if exists temps")
cursor.execute("create table temps(date text, temp int)")
cursor.execute('insert into temps values("12/01/2018",21)')
cursor.execute('insert into temps values("12/02/2018",22)')
cursor.execute('insert into temps values("12/03/2018",23)')
cursor.execute('insert into temps values("12/04/2018",24)')
cursor.execute('insert into temps values("12/05/2018",25)')
conn.row_factory = db.Row
cursor.execute("select * from temps")
rows = cursor.fetchall()
for row in rows:
   print("%s %s" % (row[0], row[1]))
cursor.execute("select avg(temp) from temps")
row = cursor.fetchone()
print("The average temp was %s" % row[0])
cursor.execute("delete from temps where temp = 25")
cursor.execute("select * from temps")
rows = cursor.fetchall()
for row in rows:
   print("%s %s" % (row[0], row[1]))
conn.close()
