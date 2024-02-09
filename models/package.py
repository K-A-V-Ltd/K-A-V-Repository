class Package:
    def __init__(self, id: int, start_loc, end_loc, weight, contact_info):
        self._id = id
        self._start_loc = start_loc
        self._end_loc = end_loc
        self._weight = weight
        self._contact_info = contact_info

    @property
    def id(self):
        return self._id

    @property
    def start_loc(self):
        return self._start_loc

    @property
    def end_loc(self):
        return self._end_loc

    @property
    def weight(self):
        return self._weight

    @property
    def contact_info(self):
        return self._contact_info

    def view(self):
        pass

    def __str__(self):
        pass
