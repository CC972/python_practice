import datetime


# Values are one-based integers
print(datetime.date(2021, 5, 17))
print(datetime.date(year=2021, month=5, day=17))

# Named constructors (factory methods implemented as class methods)
print(datetime.date.today())
print(datetime.date.fromtimestamp(1000000000))
print(datetime.date.fromordinal(720669))

# Can extract year, month and day values
d = datetime.date.today()
print(d.year)
print(d.month)
print(d.day)

# Retrieve the weekday
print(d.weekday())  # Zero-based day number, where 0 is Monday and 6 is Sunday
print(d.isoweekday())  # One-based system, where 1 is Monday and 7 is Sunday

# To return a string in ISO 8601 format
print(d.isoformat())

# For more control over date formatting of strings, use 'string format time'
# Unfortunately, both options here are not portable due to platform dependencies
print(d.strftime('%A %d %B %Y'))
print("The date is {:%A %d %B %Y}".format(d))

# A better and more Pythonic solution is to extract the date components individually
# Then pick and choose between date-specific formatting operators and date attribute access for each component
print("{date:%A} {date.day} {date:%B} {date.year}".format(date=d))

# Can retrieve limits of date instances and interval between successive dates
print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution)
