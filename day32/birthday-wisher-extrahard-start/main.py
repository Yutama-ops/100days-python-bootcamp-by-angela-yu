import random

import pandas
import datetime as dt
import smtplib
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
# read csv file
data = pandas.read_csv("birthdays.csv")
birth_dict = data.to_dict()
today = dt.datetime.now()
print(today)
year = today.year
month = today.month
day = today.day
my_email = "yutama.py@gmail.com"
my_password = "satuDuatiga!"
email_to = "yutama.iw@gmail.com"
email_v = "vienettachristina@yahoo.com"
#
# for (index, data_row) in data.iterrows():
#     print(data_row)
# print(data)

for i in range(len(birth_dict['name'])):
    if birth_dict['month'][i] == month:
        if birth_dict['day'][i] == day:
            # run the code here
            age = year - birth_dict['year'][i]
            # 3. If step 2 is true, pick a random letter from letter
            # templates and replace the [NAME] with the person's actual name from birthdays.csv
            letter = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
            the_letter = random.choice(letter)
            with open(f"letter_templates/{the_letter}") as data:
                message = data.read()
                x = message.replace("[NAME]", birth_dict['name'][i])
            # 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(my_email, my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=birth_dict['email'][i],
                    msg=f"Subject: Happy birthday {birth_dict['name'][i]}\n\n{x}"
                )






