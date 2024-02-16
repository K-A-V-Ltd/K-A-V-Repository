class WeightOverCapacityError(Exception):
    def __init__(self, message="Weight is over capacity."):
        self.message = message
        super().__init__(self.message)


class RangeOverTotalError(Exception):
    def __init__(self, message="Range is over total."):
        self.message = message
        super().__init__(self.message)


class TimeOverlapError(Exception):
    def __init__(self, message="Time overlap with existing route."):
        self.message = message
        super().__init__(self.message)
