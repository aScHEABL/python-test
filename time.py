# from datetime import datetime, timedelta

# target_city_time_in_sec = 28800

# utc_now = datetime.utcnow()

# local_time = utc_now + timedelta(seconds=target_city_time_in_sec)

# local_time_formatted = local_time.strftime("%m:%d")

# print(type(local_time_formatted))

from datetime import datetime, timedelta
timezone = 28800
current_unix = 1680318000
local_time = current_unix + timezone
formatted_current_time = datetime.utcfromtimestamp(local_time).strftime("%A %Y-%m-%d %H:%M:%S")

print(formatted_current_time)
