import smtplib

my_email = "iammadnikorejo@gmail.com"
password = "korejokk"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="madnikorejo57@gmail.com", msg="Hello")
connection.close()