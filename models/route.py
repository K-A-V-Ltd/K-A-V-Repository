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
        self.packages: list[Package] = []
        # self._truck = vehicle object
        self.eta_list: list[datetime] = self._calculate_eta()  # modify it !!!

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
            total_distance += Locations.get_distance(start_loc, end_loc)
        return total_distance

    def _calculate_eta(self):
        """
        Calculates the estimated time of arrival for each location in the locations list.

        Returns:
        - A list of datetime objects representing the estimated time of arrival for each destination.
        """
        eta_list = [self._departure_time]

        start_time = self._departure_time
        avg_speed = int(87)

        for i in range(len(self.locations) - 1):
            start_loc = self.locations[i]
            end_loc = self.locations[i + 1]
            distance = Locations.get_distance(start_loc, end_loc)
            time_taken = distance / avg_speed
            start_time += timedelta(hours=time_taken)
            eta_list.append(start_time)

        return eta_list

    def is_valid_for_package(self, start_loc, end_loc):
        """Checks if the route in question has the combination of two locations (start_loc and end_loc), while making sure that the start location is before the end location; intended to be used in conjunction with the find_suitable_route method in the ApplicationData class

        Returns:
        - a boolean"""
        try:
            start_index = self.locations.index(start_loc)
            end_index = self.locations.index(end_loc)
        except ValueError:
            return False

        return start_index < end_index

    def add_package(self, package: Package):
        self.packages.append(package)

    # finetune it
    def __str__(self):
        route_str = f"Route ID: {self.id}\n"
        for i, loc in enumerate(self.locations):
            route_str += (
                f"Location: {loc}, ETA: {self.eta_list[i].strftime('%b %d %H:%M')}\n"
            )
        return route_str
        # return f"Route ID:{self.id}: {' -> '.join([location.capitalize() for location in self.locations])}"


# left to do:
# encapsulate packages
