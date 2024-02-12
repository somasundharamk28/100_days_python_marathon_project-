import datetime as dt
import pandas as pd
import smtplib
import random


now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as data_file:
        letter = data_file.read()
        letter1 = letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user="somupersonal98@gmail.com",password="qeaulgbwnkhwidwl")
        connection.sendmail(from_addr="somupersonal98@gmail.com",to_addrs="somasundharamk28@gmail.com"
                            ,msg=f"subject:hey happybirthday \n\n {letter1}")










