import smtplib
import datetime as dt
import random


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)


    print(random_quote)
