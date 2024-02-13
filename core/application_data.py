from models.package import Package
from models.route import Route
from models.vehicles.trucks_creation import Garage


class ApplicationData:
    def __init__(self):
        self._packages: list[Package] = []
        self._routes: list[Route] = []
        self._garage = Garage #The approach might be changed.


    def add_package(self, package: Package):
        if package != None:
            self._packages.append(package)
        else:
            raise ValueError("You are trying append an empty package")

    def add_route(self, route: Route):
        if route != None:
            self._routes.append(route)
        else:
            raise ValueError("You are trying to append None as a route")

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
