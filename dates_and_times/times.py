import datetime


# Values are zero-based integers
print(datetime.time(3, 1, 2, 232))
print(datetime.time(hour=23, minute=59, second=59, microsecond=999999))

# Components of time can be retrieved
t = datetime.time(10, 32, 47, 675623)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

# ISO 8601 string representation
print(t.isoformat())

# Note that using strftime comes with portability issues due to platform dependencies
print(t.strftime('%Hh%Mm%Ss'))

# More Pythonic approach
print("{t.hour}h{t.minute}m{t.second}s".format(t=t))

# Obtain limits and resolution
print(datetime.time.max)
print(datetime.time.min)
print(datetime.time.resolution)
