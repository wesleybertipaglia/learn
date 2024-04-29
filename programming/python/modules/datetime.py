import datetime

# Get the current date
datetime.datetime.now().date()

# Get the current time
datetime.datetime.now().time()

# Get the current date and time
datetime.datetime.now()

# Create a date object with a specific year, month, and day
year, month, day = 2024, 4, 1
datetime.date(year, month, day)

# Create a time object with a specific hour, minute, and second
hour, minute, second = 12, 30, 45
datetime.time(hour, minute, second)

# Create a datetime object with a specific year, month, day, hour, minute, and second
year, month, day, hour, minute, second = 2024, 4, 1, 12, 30, 45
datetime.datetime(year, month, day, hour, minute, second)

# Format a datetime object as a string using a specified format
datetime_object = datetime.datetime.now()
format = "%Y-%m-%d %H:%M:%S"
datetime.datetime.strftime(datetime_object, format)

# Parse a string into a datetime object using a specified format
date_string = "2024-04-01 12:30:45"
format = "%Y-%m-%d %H:%M:%S"
datetime.datetime.strptime(date_string, format)
