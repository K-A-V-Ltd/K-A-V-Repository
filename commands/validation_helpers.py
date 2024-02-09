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
