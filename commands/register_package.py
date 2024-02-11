from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from models.locs_distance import Locations
from commands.validation_helpers import try_parse_float, validate_params_count


class RegisterPackageCommand(BaseCommand):

    def __init__(
        self,
        params: list[str],
        app_data: ApplicationData,
        models_factory: ModelsFactory,
    ):
        super().__init__(params, app_data)
        validate_params_count(params, 7, "RegisterPackage")
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):

        (*params,) = self.params

        start_loc = Locations.is_valid_location(params[0])
        end_loc = Locations.is_valid_location(params[1])
        weight = try_parse_float(params[2])
        first_name = params[3]
        last_name = params[4]
        phone_number = params[5]
        email = params[6]

        package = self.models_factory.create_package(
            start_loc, end_loc, weight, first_name, last_name, phone_number, email
        )
        self.app_data.add_package(package)

        return f"Package ID:{package.id} and staring location {start_loc} registered!"
