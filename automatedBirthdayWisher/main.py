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
print(year)






