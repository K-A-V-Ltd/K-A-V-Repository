from models.package import Package
from models.route import Route
from datetime import datetime


class ModelsFactory:
    def __init__(self):
        self._package_id = 1
        self._route_id = 1

    def create_package(
        self,
        start_loc: str,
        end_loc: str,
        weight: float,
        first_name: str,
        last_name: str,
        phone_number: str,
        email: str,
    ):
        package_id = self._package_id
        self._package_id += 1

        return Package(
            package_id,
            start_loc,
            end_loc,
            weight,
            first_name,
            last_name,
            phone_number,
            email,
        )

    def create_route(self, departure_time: datetime, locations: list):
        route_id = self._route_id
        self._route_id += 1

        return Route(route_id, departure_time, locations)
