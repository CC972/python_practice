# Avoid using 'from datetime import datetime' as 'datetime' would now refer to the class and not the enclosing module
# This leads to confusing results (e.g. 'datetime.time' would refer to the 'time' method of the 'datetime' class)
# Alternatively could just bind to an alternative name (e.g. 'from datetime import datetime as dt')
import datetime


# At least year, month and day must be supplied
print(datetime.datetime(2003, 5, 12, 14, 33, 22, 245323))
print(datetime.datetime(year=2003, month=5, day=12, hour=14, minute=33, second=22, microsecond=245323))

# Named constructors
# today() and now() are almost synonymous, though now() may be more precise on some systems
# Note that all these are relative to the local machine
print(datetime.datetime.today())
print(datetime.datetime.now())

# For standardised time
print(datetime.datetime.utcnow())

print(datetime.datetime.fromordinal(5))
print(datetime.datetime.fromtimestamp(3635352))
print(datetime.datetime.utcfromtimestamp(3635352))

# Can combine separate date and time objects into a single instance
d = datetime.date.today()
t = datetime.time(8, 15)
print(datetime.datetime.combine(d, t))

# Named constructor 'string parse time'
dt = datetime.datetime.strptime("Monday 6 January 2014, 12:13:31", "%A %d %B %Y, %H:%M:%S")
print(dt)

# Retrieve date and time components
print(dt.date())
print(dt.time())

# Supports the combination of the attributes and method supported by date and time individually
print(dt.day)
print(dt.isoformat())
