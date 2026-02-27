import smtplib

from pyexpat.errors import messages

my_email="fittrack45@gmail.com"
password="mmjy ansd iiui fqnk"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email, to_addrs="surojrana2059@gmail.com",
                        msg="Subject:Regarding Python Program\n\nHow was your Python training is going?")

import datetime as dt

current_time=dt.datetime.now()
year=current_time.year
month=current_time.month
time=current_time.time()
day=current_time.day
day_week=current_time.weekday()
if day== "Wednesday":
    print("Happy Days ")
print(day_week)