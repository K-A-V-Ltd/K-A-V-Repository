from models.package import Package


class Location:
    def __init__(self, name):
        self._name = name
        self.weight = 0
        self.packages: list[Package] = []
        self.time = None  # have to implement eta

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    def add_package(self, package: Package):
        self.packages.append(package)
        self._weight += package.weight

    def remove_package(self, package: Package):
        self.packages.remove(package)
        self._weight -= package.weight
