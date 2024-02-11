from models.package import Package
from models.route import Route


class ApplicationData:
    def __init__(self):
        self._packages: list[Package] = []
        self._routes: list[Route] = []

    def add_package(self, package: Package):
        self._packages.append(package)

    def add_route(self, route: Route):
        self._routes.append(route)
        

    def display_packs(self):
        for pack in self._packages:
            print(pack.weight)

    def display_routes(self):
        for route in self._routes:
            print(route.start_time)
