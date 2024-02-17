from models.vehicles.actros import Actros
from models.vehicles.man import Man
from models.vehicles.scania import Scania

Garage = [Scania() for _ in range(10)] + [Man() for _ in range(15)] + [Actros() for _ in range(15)]
