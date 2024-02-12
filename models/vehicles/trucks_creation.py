from actros import Actros
from man import Man
from scania import Scania

Scania_trucks = []
Man_truck = []
Actros_trucks = []

for x in range(9):
    truck = Scania("default", "default")
    Scania_trucks.append(truck)

for x in range(14):
    truck = Man("default", "default")
    Man_truck.append(truck)

for x in range(14):
    truck = Actros("default", "default")
    Actros_trucks.append(truck)

truck1 = Scania_trucks[0]
truck1.ending_location = "Sydney"
truck1.starting_location = "Perth"
