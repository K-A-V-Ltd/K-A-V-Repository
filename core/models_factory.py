from models.package import Package
from models.route import Route
from models.location import Location


class ModelsFactory:
    def __init__(self):
        self._package_id = 1
        self._route_id = 1

    def create_package(
        self, start_loc: Location, end_loc: Location, weight, contact_info
    ):
        package_id = self._package_id
        self._package_id += 1

        return Package(package_id, start_loc, end_loc, weight, contact_info)

    def create_route(self, start_time, locations: list[Location]):
        route_id = self._route_id
        self._route_id += 1

        return Route(route_id, start_time, locations)
