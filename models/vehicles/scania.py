from errors.vehicles_limit import OwnedVehicles
from models.vehicles.vehicle import Vehicle


class Scania(Vehicle):
    SCANIA_MAX_TRAVEL_RANGE = 8000  # Km
    SCANIA_MAX_WEIGHT_CAPACITY = 42000  # Kg

    def __init__(self):
        super().__init__()
        self._make = "Scania"
        self._range = Scania.SCANIA_MAX_TRAVEL_RANGE
        self._weight_capacity = Scania.SCANIA_MAX_WEIGHT_CAPACITY
        self._id = Vehicle.SCANIA_ID_NUMBER
        Vehicle.SCANIA_ID_NUMBER += 1

        # do we need this validation, considering we are creating the garage using list comprehension and there is no command that creates more trucks?
        if Scania.SCANIA_ID_NUMBER == 1012:
            raise OwnedVehicles("Scania")
        else:
            Scania.SCANIA_ID_NUMBER += 1
