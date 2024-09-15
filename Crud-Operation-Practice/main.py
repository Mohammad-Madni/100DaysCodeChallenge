import mysql.connector
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="db1",
)
cur=my_db.cursor()
s = "INSERT INTO book (book_id,title,price) VALUES(%s,%s,%s)"
v = [(2, "PHP", 150),(3,"java",120)]
cur.executemany(s,v)
my_db.commit()
