from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count, try_parse_int


class ViewPackageInfo(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        validate_params_count(params, 1, "ViewPackage")

    def execute(self):
        try:
            package_id = try_parse_int(self.params[0])
        except ValueError as e:
            return f"ValueError: {e}"

        package = self.app_data.find_package_by_id(package_id)

        if package == None:
            return f"There is no such package in the system."
        else:
            pack_info = package.display_info()
            return pack_info
