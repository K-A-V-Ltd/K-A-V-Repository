from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from models.location import Location
from commands.validation_helpers import try_parse_float, validate_params_count


class RegisterPackageCommand(BaseCommand):

    def __init__(
        self,
        params: list[str],
        app_data: ApplicationData,
        models_factory: ModelsFactory,
    ):
        super().__init__(params, app_data)
        validate_params_count(params, 4, "RegisterPackage")
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        # star_loc, end_loc, weight, contact_info
        (*params,) = self.params

        start_loc = Location(
            params[0]
        ).value  # in order to access the value and test; remove later
        end_loc = Location(params[1]).value  # same as above
        weight = try_parse_float(params[2])
        contact_info = params[3]

        package = self.models_factory.create_package(
            start_loc, end_loc, weight, contact_info
        )
        self.app_data.add_package(package)

        return f"Package ID:{package.id} and staring location {start_loc} registered!"
