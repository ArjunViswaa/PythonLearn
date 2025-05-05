import random
import smtplib
from datetime import *
from env import MY_EMAIL, MY_PASSWORD

now = datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    with open("quotes.txt") as quotesFile:
        quotes = quotesFile.read()
        quotes = quotes.splitlines()
        your_quote = random.choice(quotes)

    # print(your_quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Monday Motivation\n\n{your_quote}")