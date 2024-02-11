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

    def find_suitable_route(self, start_location, end_location):
        suitable_routes: list[Route] = []
        for route in self._routes:
            if route.is_valid_for_package(start_location, end_location):
                suitable_routes.append(route)
        return suitable_routes

    def find_route_by_id(self, id: int):
        for route in self._routes:
            if route.id == id:
                return route

        return None

    def display_packs(self):
        for pack in self._packages:
            print(pack.weight)

    def display_routes(self):
        for route in self._routes:
            print(route.start_time)
