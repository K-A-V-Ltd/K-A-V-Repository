"""
def is_valid_for_route(self, route: Route) -> bool:
        try:
            if self.weight_capacity <= route.total_weight:
                raise WeightOverCapacityError("Weight is over capacity.")
            elif self.range <= route.total_distance:
                raise RangeOverTotalError("Range is over total.")
            elif self.overlap(route):
                raise TimeOverlapError("Time overlap with existing route.")
            else:
                return True
        except (
            WeightOverCapacityError,
            RangeOverTotalError,
            TimeOverlapError,
        ) as e:
            print(f"Error: {e}")
            return False
"""
