import datetime


# Constructor accepts days, seconds, microseconds, milliseconds, minutes, hours and weeks
# Strongly recommended to use keyword arguments for clarity
print(datetime.timedelta(milliseconds=1, microseconds=1000))

# Note that only 3 attributes are stored internally: days, seconds and microseconds
td = datetime.timedelta(weeks=1, minutes=2, milliseconds=5500)
print(td.days)
print(td.seconds)
print(td.microseconds)

print(str(td))
print(repr(td))

# Date and time arithmetic
# Note: arithmetic on simple time objects is not supported
a = datetime.datetime(year=1996, month=8, day=21, hour=6, minute=21)
b = datetime.datetime(year=1996, month=5, day=3, hour=12, minute=3)
d = a - b
print(d)
print(d.total_seconds())

# Date from today in 3 weeks time
x = datetime.date.today() + datetime.timedelta(weeks=1) * 3
print(x)
