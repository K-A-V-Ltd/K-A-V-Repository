from models.route import Route


class Vehicle:
    SCANIA_ID_NUMBER = 1001
    Man_ID_NUMBER = 1011
    ACTROS_ID_NUMBER = 1026

    def __init__(self):

        # self._packages = []
        self.weight_capacity = None
        self.range = None
        self.routes: list[Route] = []

    # in need of refactoring
