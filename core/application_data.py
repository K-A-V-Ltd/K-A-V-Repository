from __future__ import annotations
from models.package import Package
from models.route import Route
from models.vehicles.trucks_creation import Garage
from models.vehicles.vehicle import Vehicle
from models.vehicles.actros import Actros
from models.vehicles.man import Man
from models.vehicles.scania import Scania


class ApplicationData:
    def __init__(self):
        self.unassigned_packages: list[Package] = (
            []
        )  # packages are stashed here after registration
        self.all_packages: list[Package] = (
            []
        )  # they are stashed also here for easier access to their info, might remove later and use a dictionary
        self.routes: list[Route] = []
        self._garage: list[Vehicle] = Garage  # The approach might be changed.

    def add_package(self, package: Package):
        self.unassigned_packages.append(package)
        self.all_packages.append(package)

    def add_route(self, route: Route):
        self.routes.append(route)

    # REFACTOR taking into account what is going on with in the Vehicle class
    def find_suitable_truck(self, route: Route):
        for truck in self._garage:
            if truck.is_valid_for_route(route):
                return truck

        return None

    def find_suitable_route(self, start_location, end_location):
        suitable_routes: list[Route] = []
        for route in self.routes:
            if route.is_valid_for_package(start_location, end_location):
                suitable_routes.append(route)
        return suitable_routes

    def find_route_by_id(self, id: int):
        for route in self.routes:
            if route.id == id:
                return route

        return None

    def find_package_by_id(self, id: int):
        for package in self.all_packages:
            if package.id == id:
                return package

        return None

    def display_packs(self):
        for pack in self._packages:
            print(pack.weight)

    def display_routes(self):
        for route in self._routes:
            print(route.start_time)
