from models.route import Route
from errors.truck_errors import (
    WeightOverCapacityError,
    RangeOverTotalError,
    TimeOverlapError,
)


class Vehicle:
    SCANIA_ID_NUMBER = 1001
    Man_ID_NUMBER = 1011
    ACTROS_ID_NUMBER = 1026

    def __init__(self):

        # self._packages = []
        self.make = None
        self.id = None
        self.weight_capacity = None
        self.range = None
        self.routes: list[Route] = []

        # in need of refactoring

    def is_valid_for_route(self, route: Route) -> bool:

        return not (
            self.weight_capacity <= route.total_weight
            or self.range <= route.total_distance
            or self.overlap(route)
        )

    def add_route(self, route: Route):
        self.routes.append(route)

    # refactor all validating logic by combining it and wrapping in try, except block
    # def add_route(self, new_route):
    #     if self.overlap(new_route):
    #         print("Cannot assign this truck because of time overlap.")
    #     else:
    #         self.routes.append(new_route)
    #         print("Successfully assigned.")

    def overlap(self, new_route):
        for route in self.routes:
            if self.check_time_overlap(route, new_route):
                return True
        return False

    def check_time_overlap(self, route1: Route, route2: Route):
        start_time1, end_time1 = route1.total_time
        start_time2, end_time2 = route2.total_time

        if (start_time1 <= end_time2 and end_time1 >= start_time2) or (
            start_time2 <= end_time1 and end_time2 >= start_time1
        ):
            return True
        else:
            return False

    def display_info(self):
        return "\n".join(
            [
                f"ID: {self.id}",
                f"Make: {self.make}",
                f"Weight Capacity: {self.weight_capacity}",
                f"Range: {self.range}",
            ]
        )
