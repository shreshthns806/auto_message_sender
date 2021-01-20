import pywhatkit as kit
import datetime
from datetime import date
#+918073341536

friend = input("Enter Whatsapp Number with country code- ")

def message(number, hour, time, message):
    kit.sendwhatmsg(number,message,hour,time)

date_today = date.today()

date_new_year = datetime.date(2021,12,31)

if(date_today == date_new_year):
    message(friend,0,0,"Happy New Year!")

date_christmas = datetime.date(2021,25,12)

if(date_today == date_christmas):
    message(friend,0,0,"Merry Christmas!")