from __future__ import annotations

from commands.validation_helpers import (
    ensure_valid_email,
    ensure_valid_phone,
    ensure_valid_first_name,
    ensure_valid_last_name,
    ensure_valid_weight,
)
from datetime import datetime

# from models.route import Route


class Package:

    def __init__(
        self,
        id: int,
        start_loc: str,
        end_loc: str,
        weight: float,
        first_name: str,
        last_name: str,
        phone_number: str,
        email: str,
    ):
        self._id = id
        self._start_loc = start_loc
        self._end_loc = end_loc
        self._weight = ensure_valid_weight(weight)
        self.eta = None
        self.status = None
        # self._is_delivered_status = None

        # -------contact info------------

        self._first_name = ensure_valid_first_name(first_name)
        self._last_name = ensure_valid_last_name(last_name)
        self._phone_number = ensure_valid_phone(phone_number)
        self._email = ensure_valid_email(email)

    @property
    def id(self):
        return self._id

    @property
    def start_loc(self):
        return self._start_loc

    @property
    def end_loc(self):
        return self._end_loc

    @property
    def weight(self):
        return self._weight

    @property
    def eta(self):
        return self._eta

    @eta.setter
    def eta(self, value: datetime):
        self._eta = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    # -------contact info --------

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def email(self):
        return self._email

    def display_info(self):

        eta_str = (
            "not assigned yet" if self.eta is None else self.eta.strftime("%b %d %H:%M")
        )
        status_str = "not assigned yet" if self.status is None else self.status

        return "\n".join(
            [
                f"-----INFO-----",
                f"ID: {self.id}",
                f"Weight: {self.weight}",
                f"Destination: {self.end_loc}",
                f"ETA: {eta_str}",
                f"Status: {status_str}",
            ]
        )

    def __str__(self):
        return (
            f"Package with weight: {self._weight}\n"
            f"Sent from: {self._start_loc}\n"
            f"Sent to: {self._end_loc}\n"
            f"Sent by: {self._first_name} {self._last_name}\n"
            f"Sender contact information: {self._email} Phone number: {self._phone_number}\n"
        )
