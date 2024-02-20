from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from models.locs_distance import Locations
from models.location import Location
from commands.validation_helpers import validate_minimum_params_count, validate_time
from errors.invalid_location import InvalidLocationError
from datetime import datetime


class CreateRouteCommand(BaseCommand):

    def __init__(
        self,
        params: list[str],
        app_data: ApplicationData,
        models_factory: ModelsFactory,
    ):
        super().__init__(params, app_data)
        validate_minimum_params_count(params, 5, "CreateRoute")
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        (
            month,
            date,
            time,
            *locs,
        ) = self._params

        try:
            start_str = f"{month} {date} {time}"
            departure_time = validate_time(
                datetime.strptime(start_str, "%b %d %H:%M").replace(year=2024)
            )
        except ValueError as e:
            return f"ValueError: {e}"

        try:
            locations: list[Location] = [
                Location(Locations.is_valid_location(loc_str)) for loc_str in locs
            ]
        except InvalidLocationError as e:
            return f"InvalidLocationError: {e}"

        route = self.models_factory.create_route(departure_time, locations)
        self._app_data.add_route(route)

        return (
            f"Route #{route.id} created."
        )
