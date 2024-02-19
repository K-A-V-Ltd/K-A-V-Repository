from __future__ import annotations
from models.locs_distance import Locations
from models.location import Location
from models.package import Package
# from models.vehicles.vehicle import Vehicle
from datetime import datetime, timedelta
from utils.time_abstraction import my_time


class Route:
    def __init__(self, id: int, departure_time: datetime, locations: list[Location]):
        self._id = id
        self._departure_time = departure_time
        self._locations: list[Location] = locations
        self._truck = None

        self._calculate_eta()

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
    def truck(self):
        return self._truck

    @truck.setter
    def truck(self, truck):
        self._truck = truck

    # 
    @property 
    def status(self):
        if self._departure_time > my_time():
            return "waiting to start"
        elif self._locations[-1].eta < my_time():
            return "finished"
        else:
            return "in progress"

    @property
    def total_distance(self):
        total_distance = 0
        for i in range(len(self.locations) - 1):
            start_loc = self.locations[i]
            end_loc = self.locations[i + 1]
            total_distance += Locations.get_distance(start_loc.name, end_loc.name)
        return total_distance

    @property
    def total_weight(self):
        total_weight = sum(location.weight for location in self._locations)
        return total_weight
    
    @property
    def total_time(self):
        last_eta = self._locations[-1].eta
        return self._departure_time, last_eta
    
    @property 
    def delivery_weight(self):
        next_stop_index = self._locations.index(self.next_stop)
        delivery_weight = sum(loc.weight for loc in self._locations[:next_stop_index])
        return delivery_weight

    @property
    def next_stop(self) -> Location:
        now = my_time()
        next_stop = min(self._locations, key=lambda loc: loc.eta - now)
        return next_stop
    

    def _calculate_eta(self):
        """
         Calculates the estimated time of arrival for each location in the locations list.

         Returns:
        - a dict:
        """
        self.locations[0].eta = self._departure_time
        start_time = self._departure_time
        avg_speed = int(87) # use literal, no magic numbers 

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
        location_str = " -> ".join(f"{location.name} ({location.eta.strftime('%b %d %H:%M')})" for location in self.locations)
    
        total_distance_str = f"\nTotal distance: {self.total_distance}\n"
        total_weight_str = f"Total weight: {self.total_weight}\n"
        truck_str = f'No truck assigned yet.' if self._truck == None else self._truck.display_info()
        current_stop = f'Current stop: {self.next_stop.name}'

        return route_str + location_str + total_distance_str + total_weight_str + truck_str + '\n' + current_stop

        # return f"Route ID:{self.id}: {' -> '.join([location.capitalize() for location in self.locations])}"


# left to do:
# encapsulate packages
