import datetime


# ➢ Creating Date and Time Objects
# Get current date and time

dt_now = datetime.datetime.now()
print(f"Current Time: {dt_now}")

# Get only the current date
current_date = datetime.date.today()
print("Current Date:", current_date)

# Create a date object
custom_date = datetime.date(2024, 12, 25)
print("Custom Date:", custom_date)
# Create a time object
custom_time = datetime.time(14, 30, 15)
print("Custom Time:", custom_time)
# Create a datetime object
custom_datetime = datetime.datetime(2024, 12, 25, 14, 30, 15)
print("Custom Date and Time:", custom_datetime)



now = datetime.datetime.now()
formatted = now.strftime("%A, %B %d, %Y %H:%M:%S")
print("Formatted Date and Time:", formatted)



# ➢ Parsing Strings into Date/Time Objects

# Parse a date string
date_string = "2024-12-25"
date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed Date Object:", date_object)




# ➢ Date Arithmetic - The timedelta class allows you to perform date and time arithmetic, such as adding or subtracting days:

# Current date
today = datetime.date.today()
# Add 7 days
a_week_later = today + datetime.timedelta(days=7)
print("A Week Later:", a_week_later)
# Subtract 30 days
thirty_days_ago = today - datetime.timedelta(days=30)
print("Thirty Days Ago:", thirty_days_ago)



# ➢ Getting Components of a Date/Time - You can extract individual components (year, month, day, etc.) from a date or datetime object

now = datetime.datetime.now()
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)