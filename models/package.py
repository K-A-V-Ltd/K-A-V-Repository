# Unique ID
# Start Location
# End Location
# Weight
# Customer Contact Information
from validation_helpers import valid_email, valid_phone, valid_first_name, valid_last_name, valid_package


class Package:
    PACKAGE_ID = 1

    def __init__(self, starting_location: str, ending_location: str, package_weight: int,
                 first_name: str, last_name: str, phone_number: int, email: str):
        self._starting_location = starting_location
        self._ending_location = ending_location
        self.id = Package.PACKAGE_ID
        Package.PACKAGE_ID += 1

        if not valid_package(package_weight):
            raise ValueError("Package must be above 0 KG")
        else:
            self._package_weight = package_weight

        if not valid_first_name(first_name):
            raise ValueError("You can't leave this empty")
        else:
            self._first_name = first_name

        if not valid_last_name(last_name):
            raise ValueError("You can't leave this empty")
        else:
            self._last_name = last_name

        if not valid_email(email):
            raise ValueError("This email is not valid")
        else:
            self._email = email

        if not valid_phone(phone_number):
            raise ValueError("Phone number is not valid")
        else:
            self._phone_number = phone_number

    @property
    def starting_location(self):
        return self._starting_location

    @property
    def ending_location(self):
        return self._ending_location

    @property
    def package_weight(self):
        return self._package_weight

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email

    @property
    def phone_number(self):
        return self._phone_number

    def __str__(self):
        return (f"Package with weight: {self._package_weight}\n"
                f"Sent from: {self._starting_location}\n"
                f"Sent to: {self._ending_location}\n"
                f"Sent by: {self._first_name} {self._last_name}\n"
                f"Sender contact information: {self._email} Phone number: {self._phone_number}\n")

