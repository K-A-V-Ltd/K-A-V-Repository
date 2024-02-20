from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count, try_parse_int


class AssignPackageCommand(BaseCommand):

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

        if route.truck is None:
            return "There is no truck assigned."

        if route.truck.weight_capacity < route.total_weight + package.weight:
            return (
                "The truck assigned to this route has already reached its max capacity."
            )

        route.add_package(package)
        self.app_data.unassigned_packages.remove(package)

        return f"Package #{package_id} successfully assigned to route #{route_id}."


"""
TO-DOs:
-check if a package is not already assigned 
-add a more thorough check that makes it impossible to assign a package that is not appropriate for a route (in case the employee was distracted and didn't put the right route ID)

"""
