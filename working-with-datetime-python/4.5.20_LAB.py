"""
Here's your task:
Write a program that creates a datetime object for November 4, 2020 , 14:53:00.
The object created should call the strftime method with the appropriate format to
display the following result:

2020/11/04 14:53:00
20/November/04 14:53:00 PM
Wed, 2020 Nov 04
Wednesday, 2020 November 04
Weekday: 3
Day of the year: 309
Week number of the year: 44

Note: Each result line should be created by calling the strftime method with at
least one directive in the format argument.
"""

from datetime import datetime
from time import gmtime, localtime

dt = datetime(year=2020, month=11, day=4, hour=14, minute=53, second=0)
dt_iso = (datetime.isocalendar(dt))
print(dt_iso)
dt_epoch = localtime(dt.timestamp())
print(datetime.strftime(dt, "%Y/%m/%d %H:%M:%S"))  # 2020/11/04 14:53:00
print(datetime.strftime(dt, "%y/%B/%d %H:%M:%S %p"))  # 20/November/04 14:53:00 PM
print(datetime.strftime(dt, "%a, %Y %b %d"))  # Wed, 2020 Nov 04
print(datetime.strftime(dt, "%A, %Y %B %d"))  # Wednesday, 2020 November 04
print(f"Weekday: {dt_epoch[6] + 1}")  # Weekday: 3
print(f"Day of the year: {dt_epoch[7]}")  # Day of the year: 309
print(f"Week number of the year: {dt_iso[1] - 1}")  # Week number of the year: 44
