from actros import Actros
from man import Man
from scania import Scania

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
