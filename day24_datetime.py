# Day 24: datetime and time handling for my practice

from datetime import datetime, timedelta, date
import time

# My current datetime (1)
my_now = datetime.now()
print(f"My now: {my_now}")

# My date only (2)
my_today = date.today()
print(f"My today: {my_today}")

# My creating datetime (3)
my_birthday = datetime(2000, 5, 15, 10, 30, 45)
print(f"My birthday: {my_birthday}")

# My datetime components (4)
my_dt = datetime(2025, 1, 15, 14, 30, 0)
print(f"My year: {my_dt.year}")
print(f"My month: {my_dt.month}")
print(f"My day: {my_dt.day}")
print(f"My hour: {my_dt.hour}")

# My formatting datetime (5)
my_dt = datetime(2025, 1, 15, 14, 30, 0)
my_formatted = my_dt.strftime("%Y-%m-%d %H:%M:%S")
print(f"My formatted: {my_formatted}")

# Another format
my_simple = my_dt.strftime("%m/%d/%Y")
print(f"My simple: {my_simple}")

# My parsing datetime string (6)
my_date_str = "2025-01-15 14:30:00"
my_parsed = datetime.strptime(my_date_str, "%Y-%m-%d %H:%M:%S")
print(f"My parsed: {my_parsed}")

# My timedelta (7)
my_now = datetime.now()
my_tomorrow = my_now + timedelta(days=1)
my_next_week = my_now + timedelta(weeks=1)
print(f"My tomorrow: {my_tomorrow.date()}")
print(f"My next week: {my_next_week.date()}")

# My duration calculation (8)
my_start = datetime(2025, 1, 1)
my_end = datetime(2025, 1, 15)
my_duration = my_end - my_start
print(f"My days between: {my_duration.days}")

# My timedelta in hours (9)
my_delta = timedelta(hours=2, minutes=30)
print(f"My total seconds: {my_delta.total_seconds()}")

# My working with timestamps (10)
my_timestamp = datetime.now().timestamp()
print(f"My timestamp: {my_timestamp}")

my_from_timestamp = datetime.fromtimestamp(my_timestamp)
print(f"My from timestamp: {my_from_timestamp}")

# My date arithmetic (11)
my_date = date(2025, 1, 15)
my_new_date = my_date + timedelta(days=10)
print(f"My date + 10 days: {my_new_date}")

# My weekday (12)
my_date = date(2025, 1, 15)
my_weekday = my_date.weekday()
my_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"My day: {my_days[my_weekday]}")

# My time zones (basic) (13)
from datetime import timezone, timedelta as td
my_utc = datetime.now(timezone.utc)
print(f"My UTC: {my_utc}")

# My time comparison (14)
my_date1 = datetime(2025, 1, 15)
my_date2 = datetime(2025, 1, 20)
print(f"My date1 < date2: {my_date1 < my_date2}")
print(f"My date1 == date2: {my_date1 == my_date2}")

# My age calculation (15)
my_birth = date(2000, 5, 15)
my_today = date.today()
my_age = (my_today - my_birth).days // 365
print(f"My approximate age: {my_age} years")
