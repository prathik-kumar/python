import time
from datetime import datetime, date

#printing date and time for current date/time
print(time.time())  #timestamp
print(time.localtime(time.time()))  #time struct
print(date.today())   #current date part of the ISO  8601 format
print(datetime.today()) #ISO 8601 datetime

#date-time conversions
dt1 = datetime.strptime('12/01/2020', '%m/%d/%y').isoformat()
print(dt1)

dt2 = datetime.strptime('25/12/2020', '%d/%m/%y').isoformat()
print(dt2)

#timestamp since 8.00PM on December 31st, 1969
dt3 =  datetime.fromtimestamp(0).isoformat()
print(dt3)

