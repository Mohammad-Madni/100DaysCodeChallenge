import mysql.connector
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="db1",
)
cur=my_db.cursor()
s = "SELECT * FROM book"
cur.execute(s)
result = cur.fetchall()
for rec in result:
    print(rec)
