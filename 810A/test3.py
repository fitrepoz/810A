import datetime
from datetime import date

## Part 1: Dat Arithmetic ##
date1 = "2/27/2000"
date2 = "02/27/2017"
date3 = date(2017, 1, 1)
date4 = date(2017, 10, 31)

print('What is the date three days after Feb 27, 2000?')
# set formatted date and get the day count after specified date
d = datetime.datetime.strptime(date1, '%m/%d/%Y') + datetime.timedelta(days=3)
print(d.strftime('%m/%d/%Y'))

print('What is the date three days after Feb 27, 2017?')
# set formatted date and get the day count after specified date
d = datetime.datetime.strptime(date2, '%m/%d/%Y') + datetime.timedelta(days=3)
print(d.strftime('%m/%d/%Y'))

print('How many days passed between Jan 1, 2017 and Oct 31, 2017?')
# calculate diffeence between two dates
difference = date4 - date3
print(difference.days)

## Part 2: Field separated file reader ##

