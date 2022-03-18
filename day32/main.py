# import smtplib
#
#
# my_email = "yutama.py@gmail.com"
# my_password = "satuDuatiga!"
# # SMTP object, to connect to email provider
# conn = smtplib.SMTP("smtp.gmail.com")
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     #tls = transport layer security, securing the email
#     connection.starttls()
#     #login
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="yutama.iw@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of myemial"
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
dob = dt.datetime(year=1995, month=12, day=11)
print(dob)