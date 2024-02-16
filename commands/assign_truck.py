from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count, try_parse_int


class AssignTruck(BaseCommand):

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        validate_params_count(params, 1, "AssignTruck")

    def execute(self):

        try:
            route_id = try_parse_int(self.params[0])
        except ValueError as e:
            return f"ValueError: {e}"

        route = self.app_data.find_route_by_id(route_id)

        truck = self.app_data.find_suitable_truck(route)

        if truck == None:
            return f"There are no suitable available trucks at the moment."

        truck.add_route(route)
        route.truck = truck

        return f"Truck #{truck.id} successfully assigned to route #{route.id}"

    # for checking correct initialization----delete later
    # truck_info = []
    # for truck in self.app_data._garage:
    # truck_info.append(truck.display_info())
    # return "\n\n".join(truck_info)
