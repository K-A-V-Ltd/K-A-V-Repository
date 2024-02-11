from errors.vehicles_limit import OwnedVehicles
from models.vehicles.vehicle import Vehicle


class Scania(Vehicle):

    def __init__(self, starting_location, ending_location):
        super().__init__(starting_location, ending_location)
        self.id = Vehicle.SCANIA_ID_NUMBER
        Vehicle.SCANIA_ID_NUMBER += 1

        if Scania.SCANIA_ID_NUMBER >= 1010:
            raise OwnedVehicles("Scania")
        else:
            Scania.SCANIA_ID_NUMBER += 1

