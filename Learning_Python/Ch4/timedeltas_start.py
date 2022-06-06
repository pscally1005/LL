#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# TODO: construct a basic timedelta and print it
# print(timedelta(days=365, hours=5, minutes=1))

# # TODO: print today's date
# now = datetime.now()
# print("Today is:", now)

# # TODO: print today's date one year from now
# print("One year from now it will be:", str(now + timedelta(days=365)))

# # TODO: create a timedelta that uses more than one argument
# print("In 2 weeks and 3 days it will be:", str(now + timedelta(weeks=2, days=3)))

# # TODO: calculate the date 1 week ago, formatted as a string
# # print("1 week ago is was:", str(now - timedelta(weeks=1)))
# t = datetime.now() - timedelta(weeks=1)
# s = t.strftime("%A %B %d %Y")
# print("1 week ago it was:", s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, month=4, day=1)
if afd < today:
    print("April Fool's Day already happened this year")
    print("The next April fools day is in", str(365+(afd-today).days), "days")
    afd = afd.replace(year = today.year + 1)
else:
    print("April Fool's Day has not happened yet this year")
    print("April Fool's Day is in", (afd-today).days, "days")

# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year

# TODO: Now calculate the amount of time until April Fool's Day  

