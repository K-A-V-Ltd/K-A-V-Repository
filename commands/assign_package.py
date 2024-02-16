from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count, try_parse_int


class AssignPackage(BaseCommand):

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        validate_params_count(params, 2, "AssignPackage")

    def execute(self):

        package_id, route_id = self.params

        try:
            package_id = try_parse_int(package_id)
            route_id = try_parse_int(route_id)
        except ValueError as e:
            return f"ValueError: {e}"

        package = self.app_data.find_package_by_id(package_id)

        if package is None:
            return "There is no such package in the system."

        route = self.app_data.find_route_by_id(route_id)

        if route is None:
            return "There is no such route in the system."

        route.add_package(package)
        self.app_data.unassigned_packages.remove(package)

        return f"Package #{package_id} successfully assigned to route #{route_id}."
