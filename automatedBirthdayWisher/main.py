##################### Normal Starting Project ######################
import csv
import random
import pandas as pd
from datetime import datetime
import smtplib

MY_EMAIL = "appbrewarycourse@gmail.com"
MY_PASSWORD = "password"

now = datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    random_number = random.randint(1, 3)
    file_path = f"letter_templates/letter_{random_number}.txt"
    with open(file_path) as file:
        content = file.read()
        content.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday \n\n{content}")



