from custom_errors import OwnedVehicles
from models.vehicles.vehicle import Vehicle


class Scania(Vehicle):

    def __init__(self, starting_location, ending_location):
        super().__init__(starting_location, ending_location)
        if Scania.SCANIA_ID_NUMBER >= 1010:
            raise OwnedVehicles("Scania")
        else:
            Scania.SCANIA_ID_NUMBER += 1









