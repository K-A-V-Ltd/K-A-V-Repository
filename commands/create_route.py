from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from models.location import Location
from commands.validation_helpers import (
    try_parse_float,
    validate_params_count,
    validate_minimum_params_count,
)


class CreateRouteCommand(BaseCommand):

    def __init__(
        self,
        params: list[str],
        app_data: ApplicationData,
        models_factory: ModelsFactory,
    ):
        super().__init__(params, app_data)
        validate_minimum_params_count(params, 3, "CreateRoute")
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        (
            start_time,
            *locs,
        ) = self._params

        # figure out validation for start time (00:00 format)

        locations = [
            Location[loc_str] for loc_str in locs
        ]  # validate that each location is valid

        route = self.models_factory.create_route(start_time, locations)


# a way to parse time format -> put into validation helpers

# from datetime import datetime, timedelta

# Starting time string
# start_time_str = "Oct 10 22:30"

# Parse the string into a datetime object
# start_datetime = datetime.strptime(start_time_str, "%b %d %H:%M")

# for using later in the program
# later_datetime = start_datetime + timedelta(hours=2) - this is how why can calculate the times for each stop later on in the program
