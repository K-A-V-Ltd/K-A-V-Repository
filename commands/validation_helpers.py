# to be implemented
from datetime import datetime
from errors.invalid_params import InvalidParamsError
from errors.invalid_minimum_params import InvalidMinimumParams
from errors.invalid_time import InvalidTime


def validate_params_count(params: list[str], count: int, cmd_name: str):
    if len(params) != count:
        raise InvalidParamsError(cmd_name, count)


def validate_minimum_params_count(params: list[str], count: int, cmd_name: str):
    if len(params) < count:
        raise InvalidMinimumParams(cmd_name, count)


def validate_time(departure_time: datetime):
    if departure_time < datetime.now():
        raise InvalidTime(departure_time)
    else:
        return departure_time


def try_parse_float(s):
    try:
        return float(s)
    except:
        raise ValueError("Invalid value for weight. Should be a number.")


def try_parse_int(s):
    try:
        return int(s)
    except:
        raise ValueError("Invalid value for ID. Should be an integer.")


# ---------VALIDATIONS FOR CLASS PACKAGE------------


def ensure_valid_weight(value):
    if value <= 0.5:
        raise ValueError("Weight should be above 0.5kg")

    return value


def ensure_valid_phone(value):
    if len(value) != 10:
        raise ValueError("Phone number should be 10 digits long.")
    if not value.isdigit():
        raise ValueError("Phone number should contain only digits ")

    return value


# add a length requirement as well


def ensure_valid_email(value):
    if not ("@gmail.com" in value or "@yahoo.com" in value):
        raise ValueError("Email should contain '@gmail.com' or '@yahoo.com'")

    return value


def ensure_valid_first_name(value):
    if not 2 <= len(value) <= 10:
        raise ValueError("First name should be between 2 and 10 characters long.")

    return value


def ensure_valid_last_name(value):
    if not 2 <= len(value) <= 10:
        raise ValueError("Last name should be between 2 and 10 characters long.")

    return value
