from errors.invalid_location import InvalidLocation


class Locations:

    CITY = {
        "sydney": 0,
        "melbourne": 1,
        "adelaide": 2,
        "alicesprings": 3,
        "brisbane": 4,
        "darwin": 5,
        "perth": 6,
    }

    DISTANCE = [
        [0, 877, 1376, 2762, 909, 3935, 4016],
        [877, 0, 725, 2255, 1765, 3752, 3509],
        [1376, 725, 0, 1530, 1927, 3027, 2785],
        [2762, 2255, 1530, 0, 2993, 1497, 2481],
        [909, 1765, 1927, 2993, 0, 3426, 4311],
        [3935, 3752, 3027, 1497, 3426, 0, 4025],
        [4016, 3509, 2785, 2481, 4311, 4025, 0],
    ]

    @staticmethod
    def is_valid_location(location: str) -> str:
        if location.lower() not in Locations.CITY:
            raise InvalidLocation(location)
        return location.capitalize()

    @staticmethod
    def get_distance(start_loc: str, end_loc: str) -> int:
        start = start_loc.lower()
        end = end_loc.lower()
        return Locations.DISTANCE[Locations.CITY[start]][Locations.CITY[end]]
