# to be implemented
from errors.invalid_params import InvalidParams
from errors.invalid_minimum_params import InvalidMinimumParams


def validate_params_count(params: list[str], count: int, cmd_name: str):
    if len(params) != count:
        raise InvalidParams(cmd_name, count)


def validate_minimum_params_count(params: list[str], count: int, cmd_name: str):
    if len(params) < count:
        raise InvalidMinimumParams(cmd_name, count)


def try_parse_float(s):
    try:
        return float(s)
    except:
        raise ValueError("Invalid value for price. Should be a number.")


def try_parse_int(s):
    try:
        return int(s)
    except:
        raise ValueError("Invalid value for mililitres. Should be an integer.")

def valid_phone(value):
    """
    This function takes value as a parameter and returns True if it's length is acceptable.
    """
    if len(str(value)) >= 6:
        return True


def valid_email(value):
    """
    This function takes value as a parameter and returns True if the domain is in the of acceptable domains.
    """

    if ("@gmail.com" in value or "@yahoo.com" in value) and len(value) >= 12:
        return True


def valid_first_name(value):
    """
    This function takes value as a parameter and returns True if the name contains at least 1 letter.
    """
    if len(value) >= 1:
        return True


def valid_last_name(value):
    """
    This function takes value as a parameter and returns True if the name contains at least 1 letter.
    """
    if len(value) >= 1:
        return True


def valid_package(value):
    """
    This function takes value as a parameter and returns True if it's above 0.
    """
    if 1 <= value:
        return True
