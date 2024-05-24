# import smtplib
#
# my_email = "iammadnikorejo@gmail.com"
# password = "nczavdnhluvlzsel"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="madnikorejo57@gmail.com",
#         msg="Subject:Hello\n\n"
#             " this is body of my email!")
import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
week = now.weekday()
print(year)
print(month)
print(week)
date_of_birth = dt.datetime(year=1999, month=6, day=15)
print(date_of_birth)





