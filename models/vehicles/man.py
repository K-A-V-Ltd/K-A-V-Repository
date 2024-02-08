from custom_errors import OwnedVehicles
from models.vehicles.vehicle import Vehicle


class Man(Vehicle):

    def __init__(self, starting_location, ending_location):
        super().__init__(starting_location, ending_location)
        if Man.Man_ID_NUMBER >= 1025:
            raise OwnedVehicles("Man")
        else:
            Man.Man_ID_NUMBER += 1


