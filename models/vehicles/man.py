from errors.vehicles_limit import OwnedVehicles
from models.vehicles.vehicle import Vehicle


class Man(Vehicle):
    Man_MAX_TRAVEL_RANGE = 10000  # Km
    MAN_MAX_WEIGHT_CAPACITY = 37000  # Kg

    def __init__(self):
        super().__init__()
        self.range = Man.Man_MAX_TRAVEL_RANGE
        self.weight_capacity = Man.MAN_MAX_WEIGHT_CAPACITY
        self.id = Vehicle.Man_ID_NUMBER
        Vehicle.Man_ID_NUMBER += 1
        if Man.Man_ID_NUMBER == 1027:
            raise OwnedVehicles("Man")
        else:
            Man.Man_ID_NUMBER += 1
