class Vehicle:
    SCANIA_ID_NUMBER = 1001
    Man_ID_NUMBER = 1011
    ACTROS_ID_NUMBER = 1026

    SCANIA_MAX_TRAVEL_RANGE = 8000  # Km
    Man_MAX_TRAVEL_RANGE = 10000  # Km
    ACTROS_MAX_TRAVEL_RANGE = 13000  # Km

    SCANIA_MAX_WEIGHT_CAPACITY = 42000  # Kg
    MAN_MAX_WEIGHT_CAPACITY = 37000  # Kg
    ACTROS_MAX_WEIGHT_CAPACITY = 26000  # Kg

    def __init__(self, starting_location: str, ending_location: str):
        self._starting_location = starting_location
        self._ending_location = ending_location
        self._packages = []

    @property
    def starting_location(self):
        return self._starting_location

    @starting_location.setter
    def starting_location(self, value):
        self._starting_location = value

    @property
    def ending_location(self):
        return self._ending_location

    @ending_location.setter
    def ending_location(self, value):
        self._ending_location = value

    @property
    def packages(self):
        return self._packages

    def add_package(self, value):
        """
        This function takes value as a parameter and adds it to the package list. If the value is None it raises an
        error.
        """
        if value is not None:
            self._packages.append(value)
        else:
            raise ValueError("We don't deliver empty packages!")

    def remove_package(self, value):
        """
        This function takes value as a parameter and removes it from the storage if it's there. If it's not it raises
        error.
        """
        if value in self._packages:
            self._packages.remove(value)
        else:
            raise ValueError("We apologise, but we possess no such package in our storage.")
