# Need to use tzinfo for "aware" objects (as opposed to "naive")
# There is no exhaustive timezone data in Python, although rudimentary support is provided
# Otherwise would need third-party modules like pytz or dateutil
import datetime

# timezone is a concrete implementation of tzinfo (abstract interface)
cet = datetime.timezone(datetime.timedelta(hours=1), "CET")
print(cet)

# Can now specify this tzinfo instance when constructing a time/datetime object
departure = datetime.datetime(year=2021, month=5, day=27, hour=11, minute=30, tzinfo=cet)
arrival = datetime.datetime(year=2021, month=5, day=27, hour=13, minute=5, tzinfo=datetime.timezone.utc)
duration = arrival - departure
print(duration)
