"""Read amount of free disk space in current working directory.
Using the extended iter() form to create infinite sequence."""

from pathlib import Path
from shutil import disk_usage
import time
import datetime


# Current working directory
cwd = Path.cwd()


def free_space():
    """Wrap call to disk in another function to make a zero-argument callable"""
    return disk_usage(cwd).free


free_space_readings = iter(free_space, None)
timestamps = iter(datetime.datetime.now, None)


for timestamp, free_bytes in zip(timestamps, free_space_readings):
    print(timestamp, free_bytes)
    time.sleep(1.0)





