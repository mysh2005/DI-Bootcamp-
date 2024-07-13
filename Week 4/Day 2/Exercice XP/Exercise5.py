from datetime import datetime

def time_until_new_year():
    actual_datetime = datetime.now()
    next_year = actual_datetime.year + 1 if actual_datetime.month == 12 else actual_datetime.year
    new_year = datetime(next_year + 1, 1, 1)
    time_diff = new_year - actual_datetime

    days = time_diff.days
    seconds = time_diff.seconds

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    print(f"The 1st of January is in {days} days, {hours:02}:{minutes:02}:{seconds:02} hours.")

time_until_new_year()
