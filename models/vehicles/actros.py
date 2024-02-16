from errors.vehicles_limit import OwnedVehicles
from models.vehicles.vehicle import Vehicle


class Actros(Vehicle):
    ACTROS_MAX_TRAVEL_RANGE = 13000  # Km
    ACTROS_MAX_WEIGHT_CAPACITY = 26000  # Kg

    def __init__(self):
        super().__init__()
        self.make = "Actros"
        self.range = Actros.ACTROS_MAX_TRAVEL_RANGE
        self.weight_capacity = Actros.ACTROS_MAX_WEIGHT_CAPACITY
        self.id = Vehicle.ACTROS_ID_NUMBER
        Vehicle.ACTROS_ID_NUMBER += 1

        if Actros.ACTROS_ID_NUMBER == 1042:
            raise OwnedVehicles("Actros")
        else:
            Actros.ACTROS_ID_NUMBER += 1


# to-do:
# encapsulate properties, readonly, only getters
