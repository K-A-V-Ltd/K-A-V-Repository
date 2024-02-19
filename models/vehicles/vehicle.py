from models.route import Route


class Vehicle:
    SCANIA_ID_NUMBER = 1001
    Man_ID_NUMBER = 1011
    ACTROS_ID_NUMBER = 1026

    def __init__(self):

        self._make = None
        self._id = None
        self._weight_capacity = None
        self._range = None
        self._routes: list[Route] = []

    @property
    def make(self):
        return self._make

    @property
    def id(self):
        return self._id

    @property
    def weight_capacity(self):
        return self._weight_capacity

    @property
    def range(self):
        return self._range

    @property
    def routes(self):
        return tuple(self._routes)

    def add_route(self, route: Route):
        self._routes.append(route)

    def is_valid_for_route(self, route: Route) -> bool:

        return not (
            self.weight_capacity <= route.total_weight
            or self._range <= route.total_distance
            or self.overlap(route)
        )

    def overlap(self, new_route) -> bool:
        for route in self._routes:
            if self.check_time_overlap(route, new_route):
                return True
        return False

    def check_time_overlap(self, route1: Route, route2: Route) -> bool:
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
                f"Range: {self._range}",
            ]
        )
