from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from models.locs_distance import Locations
from commands.validation_helpers import try_parse_float, validate_params_count
from errors.invalid_location import InvalidLocationError
from errors.invalid_params import InvalidParamsError


class SearchRouteCommand(BaseCommand):

    def __init__(
        self,
        params: list[str],
        app_data: ApplicationData,
    ):
        super().__init__(params, app_data)
        validate_params_count(params, 2, "SearchRoute")

    def execute(self):
        start_loc, end_loc = self.params

        try:
            start_loc = Locations.is_valid_location(start_loc)
            end_loc = Locations.is_valid_location(end_loc)
        except InvalidLocationError as e:
            return f"Invalid location: {e}"

        suitable_routes = self._app_data.find_suitable_route(start_loc, end_loc)

        if not suitable_routes:
            return f"There is no suitable route for this package."
        else:
            return "\n".join([str(route) for route in suitable_routes])
