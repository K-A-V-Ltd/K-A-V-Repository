from errors.vehicles_limit import OwnedVehicles
from models.vehicles.vehicle import Vehicle


class Actros(Vehicle):

    def __init__(self, starting_location, ending_location):
        super().__init__(starting_location, ending_location)
        self.id = Vehicle.ACTROS_ID_NUMBER
        Vehicle.ACTROS_ID_NUMBER += 1

        if Actros.ACTROS_ID_NUMBER == 1041:
            raise OwnedVehicles("Actros")
        else:
            Actros.ACTROS_ID_NUMBER += 1


