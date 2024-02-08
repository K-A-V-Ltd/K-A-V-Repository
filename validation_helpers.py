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
    if "@gmail.com" in value or "@yahoo.com" in value and len(value) >= 13:
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
