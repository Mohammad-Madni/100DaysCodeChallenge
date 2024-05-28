import smtplib
import datetime as dt
import random

MY_GMAIL = "appbrewarycourse@gmail.com"
MY_PASSWORD = "password123()"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)
    print(random_quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_GMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_GMAIL,
                            to_addrs=MY_GMAIL,
                            msg=f"Subject:Monday Motivation\n\n{random_quote}")


