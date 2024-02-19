from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class ViewActiveRoutesCommand(BaseCommand):
    def execute(self):

        formatted_routes = ""

        for route in self.app_data.routes:
            if route.status == "in progress":
                formatted_routes += f"{str(route)}\nDelivery Weight: {route.delivery_weight}\nNext Stop: {route.next_stop.name}\n\n"

        if not formatted_routes:
            return "No routes are currently in progress."

        return formatted_routes
