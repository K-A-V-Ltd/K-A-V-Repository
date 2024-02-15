from __future__ import annotations
from models.locs_distance import Locations
from models.location import Location
from models.package import Package
from datetime import datetime, timedelta


class Route:
    def __init__(self, id: int, departure_time: datetime, locations: list[Location]):
        self._id = id
        self._departure_time = departure_time
        self._locations: list[Location] = locations
        # self._truck = vehicle object

        self._calculate_eta()
        # self.packages: list[Package] = [] - do we need them ?

    @property
    def id(self):
        return self._id

    @property
    def departure_time(self):
        return self._departure_time

    @property
    def locations(self):
        return tuple(self._locations)

    @property
    def total_distance(self):
        total_distance = 0
        for i in range(len(self.locations) - 1):
            start_loc = self.locations[i]
            end_loc = self.locations[i + 1]
            total_distance += Locations.get_distance(start_loc.name, end_loc.name)
        return total_distance

    def _calculate_eta(self):
        """
         Calculates the estimated time of arrival for each location in the locations list.

         Returns:
        - a dict:
        """
        self.locations[0].eta = self._departure_time
        start_time = self._departure_time
        avg_speed = int(87)

        for i in range(len(self.locations) - 1):
            start_loc = self.locations[i]
            end_loc = self.locations[i + 1]
            distance = Locations.get_distance(start_loc.name, end_loc.name)
            time_taken = distance / avg_speed
            start_time += timedelta(hours=time_taken)
            end_loc.eta = start_time

    def is_valid_for_package(self, start_loc, end_loc) -> bool:
        """Checks if the route in question has the combination of two locations (start_loc and end_loc), while making sure that the start location is before the end location; intended to be used in conjunction with the find_suitable_route method in the ApplicationData class

        Returns:
        - a boolean"""

        start_index = None
        end_index = None
        for i, loc in enumerate(self.locations):
            if loc.name == start_loc:
                start_index = i
            elif loc.name == end_loc:
                end_index = i

        if start_index is None or end_index is None:
            return False

        return start_index < end_index

    def add_package(self, package: Package):
        for location in self.locations:
            if package.end_loc == location.name:
                location.add_package(package)

    # finetune it
    def __str__(self):
        route_str = f"Route ID: {self.id}\n"
        location_str = " -> ".join(location.name for location in self.locations)

        return route_str + location_str

        # return f"Route ID:{self.id}: {' -> '.join([location.capitalize() for location in self.locations])}"


# left to do:
# encapsulate packages
