from datetime import datetime

from commands.validation_helpers import validate_time

VALID_FIRST_NAME = "Alex"
VALID_LAST_NAME = "Daskalov"
VALID_PHONE_NUMBER = "1111111111"
VALID_EMAIL = "AlexD@gmail.com"
VALID_STARTING_LOCATION = "Sydney"
VALID_ENDING_LOCATION = "Melbourne"
VALID_PACKAGE = 35.5
ID = 1
VALID_RANGE = 20000

month = "Mar"
date = "11"
time = "12:30"

start_str = f"{month} {date} {time}"
DEPARTURE_TIME = validate_time(
                datetime.strptime(start_str, "%b %d %H:%M").replace(year=2025))




month = "June"
date = "12"
time = "11:40"
start_str2 = f"{month} {date} {time}"
DEPARTURE_TIME2 = validate_time(
                datetime.strptime(start_str, "%b %d %H:%M").replace(year=2024))

