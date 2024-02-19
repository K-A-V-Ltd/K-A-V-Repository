from errors.vehicles_limit import OwnedVehicles
from models.vehicles.vehicle import Vehicle


class Actros(Vehicle):
    ACTROS_MAX_TRAVEL_RANGE = 13000  # Km
    ACTROS_MAX_WEIGHT_CAPACITY = 26000  # Kg

    def __init__(self):
        super().__init__()
        self._make = "Actros"
        self._range = Actros.ACTROS_MAX_TRAVEL_RANGE
        self._weight_capacity = Actros.ACTROS_MAX_WEIGHT_CAPACITY
        self._id = Vehicle.ACTROS_ID_NUMBER
        Vehicle.ACTROS_ID_NUMBER += 1

        # do we need this? look at comment in Scania class

        if Actros.ACTROS_ID_NUMBER == 1042:
            raise OwnedVehicles("Actros")
        else:
            Actros.ACTROS_ID_NUMBER += 1
