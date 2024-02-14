from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class ViewUnassignedPackages(BaseCommand):
    def execute(self):
        if len(self.app_data.unassigned_packages) == 0:
            return "There are no unassigned packages at the moment."
        else:
            return "\n".join(
                f"ID: {package.id} Location: {package.start_loc}"
                for package in self.app_data.unassigned_packages
            )
