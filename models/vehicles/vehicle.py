from models.route import Route


class Vehicle:
    SCANIA_ID_NUMBER = 1001
    Man_ID_NUMBER = 1011
    ACTROS_ID_NUMBER = 1026

    def __init__(self):

        # self._packages = []
        self.weight = None
        self.range = None
        self.routes: list[Route] = []

    # in need of refactoring

    @property
    def unused_capacity(self):
        used_capacity = sum([x.weight for x in self._packages])
        return self.weight - used_capacity

    @property
    def packages(self):
        return self._packages

    def add_package(self, value):
        """
        This function takes value as a parameter and adds it to the package list. If the value is None it raises an
        error.
        """
        if value is not None:
            self._packages.append(value)
        else:
            raise ValueError("We don't deliver empty packages!")

    def remove_package(self, value):
        """
        This function takes value as a parameter and removes it from the storage if it's there. If it's not it raises
        error.
        """
        if value in self._packages:
            self._packages.remove(value)
        else:
            raise ValueError(
                "We apologise, but we possess no such package in our storage."
            )
