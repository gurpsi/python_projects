import datetime as dt

gvr = dt.date(1956,1,31) # Guido Van Rossum DOB python creator.
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)

mill = dt.date(2000,1,1)
revolution = dt.timedelta(100) # Timedelta is a module to add or subtract number of days.
print(mill+revolution)
print(mill-revolution)

# By default python's date format is YYYY-MM-DD, which we can change.
print(gvr.strftime("%A, %B %d, %Y"))

# Or this can also be done as:
message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))

launch_date = dt.date(2017, 3, 30)
launch_time = dt.time(22, 27, 0)
launch_datetime = dt.datetime(2017, 3, 30, 22, 27, 0)

print(launch_date)
print(launch_time)
print(launch_datetime)

now = dt.datetime.today()
print(now)
print(now.microsecond)