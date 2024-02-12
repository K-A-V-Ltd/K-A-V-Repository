from errors.vehicles_limit import OwnedVehicles
from models.vehicles.vehicle import Vehicle


class Man(Vehicle):

    def __init__(self, starting_location, ending_location):
        super().__init__(starting_location, ending_location)
        self.id = Vehicle.Man_ID_NUMBER
        Vehicle.Man_ID_NUMBER += 1
        if Man.Man_ID_NUMBER == 1026:
            raise OwnedVehicles("Man")
        else:
            Man.Man_ID_NUMBER += 1


