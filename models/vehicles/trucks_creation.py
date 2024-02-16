from models.vehicles.actros import Actros
from models.vehicles.man import Man
from models.vehicles.scania import Scania




Garage = []

for x in range(10):
    truck = Scania()
    Garage.append(truck)

for x in range(15):
    truck = Man()
    Garage.append(truck)

for x in range(15):
    truck = Actros()
    Garage.append(truck)

