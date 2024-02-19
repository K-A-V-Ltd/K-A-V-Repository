from datetime import datetime

from commands.validation_helpers import validate_time
from models.package import Package

"***************************************"
#       "Package testing variables"
VALID_FIRST_NAME = "Alex"
VALID_LAST_NAME = "Daskalov"
VALID_PHONE_NUMBER = "1111111111"
VALID_EMAIL = "AlexD@gmail.com"
VALID_STARTING_LOCATION = "Sydney"
VALID_ENDING_LOCATION = "Melbourne"
VALID_PACKAGE = 1.5
VALID_ID = 1

VALID_PACKAGE = Package(1, VALID_STARTING_LOCATION, VALID_ENDING_LOCATION, VALID_PACKAGE,
                          VALID_FIRST_NAME, VALID_LAST_NAME,
                          VALID_PHONE_NUMBER, VALID_EMAIL,)



"**************************************"
#       "Truck testing variables"
VALID_RANGE = 20000






"**************************************"
#   "Datetime testing variables"
"Object 1"
month = "Mar"
date = "11"
time = "12:30"

start_str = f"{month} {date} {time}"
DEPARTURE_TIME = validate_time(
                datetime.strptime(start_str, "%b %d %H:%M").replace(year=2025))


"Object 2"
month = "June"
date = "12"
time = "11:40"
start_str2 = f"{month} {date} {time}"
DEPARTURE_TIME2 = validate_time(
                datetime.strptime(start_str, "%b %d %H:%M").replace(year=2024))

