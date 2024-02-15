from __future__ import annotations

from models.package import Package  # causing problems circular imports


class Location:
    def __init__(self, name: str):
        self._name = name
        self.weight = 0
        self.packages: list[Package] = []  # circular imports
        self.eta = None  # have to implement eta

    @property
    def name(self):
        return self._name

    @property
    def eta(self):
        return self._eta

    @eta.setter
    def eta(self, value):
        self._eta = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value: int):
        self._weight = value

    def add_package(self, package: Package):
        self.packages.append(package)
        package.eta = self.eta
        package.status = "assigned"  # change later (different stages)
        self._weight += package.weight

    def remove_package(self, package):
        self.packages.remove(package)
        self._weight -= package.weight
