# send motivational quote vie email on the current weekday
# use datetime modules to obtain the current day of the week
import datetime as dt
import random
import smtplib

date = dt.datetime.now()
year = date.year
month = date.month
day = date.day
dotw = date.weekday()

# open the quotes.txt file and obtain list of quotes
with open("quotes.txt", "r") as data:
    quotes = data.readlines()

# use random module to pick a random quote from your list of quotes
qotd = random.choice(quotes)

# use smtplib to send the email to yourself
my_email = "yutama.py@gmail.com"
my_password = "satuDuatiga!"
email_to = "yutama.iw@gmail.com"
email_v = "vienettachristina@yahoo.com"
print(dotw)
if dotw == 5:
    print("HAHA")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(
            user=my_email,
            password=my_password
        )
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email_v,
            msg=f"Subject: Quote of the day\n\n{qotd}"
        )




