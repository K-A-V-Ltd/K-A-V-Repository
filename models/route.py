from models.location import Location


class Route:
    def __init__(self, id: int, start_time, locations: list[Location]):
        self._id = id
        self._start_time = start_time
        self._locations = locations
        self._trucks = []

    @property
    def id(self):
        return self._id

    @property
    def start_time(self):
        return self._start_time
