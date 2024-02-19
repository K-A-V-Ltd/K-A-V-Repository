from commands.register_package import RegisterPackageCommand
from commands.create_route import CreateRouteCommand
from commands.search_route import SearchRouteCommand
from commands.view_unassigned import ViewUnassignedPackagesCommand
from commands.view_pack_info import ViewPackageInfoCommand
from commands.assign_package import AssignPackageCommand
from commands.assign_truck import AssignTruckCommand
from core.models_factory import ModelsFactory
from errors.invalid_command import InvalidCommandError


class CommandFactory:
    def __init__(self, data):
        self._app_data = data
        self._models_factory = ModelsFactory()

    @property
    def app_data(self):
        return self._app_data

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "registerpackage":
            return RegisterPackageCommand(params, self._app_data, self._models_factory)
        if cmd.lower() == "createroute":
            return CreateRouteCommand(params, self._app_data, self._models_factory)
        if cmd.lower() == "searchroute":
            return SearchRouteCommand(params, self._app_data)
        if cmd.lower() == "viewunassignedpackages":
            return ViewUnassignedPackagesCommand(params, self._app_data)
        if cmd.lower() == "viewpackageinfo":
            return ViewPackageInfoCommand(params, self._app_data)
        if cmd.lower() == "assignpackage":
            return AssignPackageCommand(params, self._app_data)
        if cmd.lower() == "assigntruck":
            return AssignTruckCommand(params, self._app_data)

        raise InvalidCommandError(cmd)
