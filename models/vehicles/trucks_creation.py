from models.vehicles.actros import Actros
from models.vehicles.man import Man
from models.vehicles.scania import Scania

# can't we have just one list Garage, instead of nested lists for easier access

Scania_trucks = []
Man_truck = []
Actros_trucks = []

for x in range(10):
    truck = Scania()
    Scania_trucks.append(truck)

for x in range(15):
    truck = Man()
    Man_truck.append(truck)

for x in range(15):
    truck = Actros()
    Actros_trucks.append(truck)

Garage = [Scania_trucks, Man_truck, Actros_trucks]
