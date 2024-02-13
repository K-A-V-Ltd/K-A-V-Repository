from datetime import datetime

VALID_FIRST_NAME = "Alex"
VALID_LAST_NAME = "Daskalov"
VALID_PHONE_NUMBER = "1111111111"
VALID_EMAIL = "AlexD@gmail.com"
VALID_STARTING_LOCATION = "Sydney"
VALID_ENDING_LOCATION = "Melbourne"
VALID_PACKAGE = 35.5


start_str = f"{"Mar"} {11} {"12:30"}"
DEPARTURE_TIME = datetime.strptime(start_str, "%b %d %H:%M").replace(year=2024)
LOCATIONS = [VALID_STARTING_LOCATION, VALID_ENDING_LOCATION]