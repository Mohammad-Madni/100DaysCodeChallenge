import smtplib
import datetime as dt
import random

MY_GMAIL = "appbrewarycourse@gmail.com"
MY_PASSWORD = "xhxtkolbjhwdnvrx"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_GMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_GMAIL,
                            to_addrs=MY_GMAIL,
                            msg=f"Subject:Monday Motivation\n\n{random_quote}")


print(random_quote)

