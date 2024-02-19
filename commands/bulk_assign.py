from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import validate_minimum_params_count, try_parse_int


class BulkAssignCommand(BaseCommand):

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        validate_minimum_params_count(params, 4, "BulkAssign")

    def execute(self):
        route_id, *package_ids = self._params

        try:
            route_id = try_parse_int(route_id)
            pack_ids = [try_parse_int(package_id) for package_id in package_ids]
        except ValueError as e:
            return f"ValueError: {e}"

        route = self.app_data.find_route_by_id(route_id)

        if route is None:
            return "There is no such route in the system."

        assigned = []
        not_found = []

        for package_id in pack_ids:
            package = self.app_data.find_package_by_id(package_id)
            if package is None:
                not_found.append(package_id)
            else:
                route.add_package(package)
                self.app_data.unassigned_packages.remove(package)
                assigned.append(package_id)

        if not_found:
            return f"The following packages were not found: {', '.join(map(str, not_found))}."
        else:
            return (
                f"{len(assigned)} packages successfully assigned to route #{route_id}."
            )
