##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import random
import smtplib
import pandas
from env import MY_EMAIL, MY_PASSWORD

today = dt.datetime.now()
our_data = pandas.read_csv("birthdays.csv")

for index, row in our_data.iterrows():
    if row["month"] == today.month and row["day"] == today.day:
        birthday_person = row["name"]
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path) as file:
            contents = file.read()
            contents = contents.replace("[NAME]", birthday_person)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=row["email"], msg=f"Subject:Happy Birthday {birthday_person}!!\n\n{contents}")