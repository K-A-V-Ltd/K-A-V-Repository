from commands.register_package import RegisterPackageCommand
from commands.create_route import CreateRouteCommand
from commands.search_route import SearchRouteCommand
from commands.view_unassigned import ViewUnassignedPackages
from commands.view_pack_info import ViewPackageInfo
from commands.assign_package import AssignPackage
from core.models_factory import ModelsFactory
from errors.invalid_command import InvalidCommand


class CommandFactory:
    def __init__(self, data):
        self._app_data = data
        self._models_factory = ModelsFactory()

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "registerpackage":
            return RegisterPackageCommand(params, self._app_data, self._models_factory)
        if cmd.lower() == "createroute":
            return CreateRouteCommand(params, self._app_data, self._models_factory)
        if cmd.lower() == "searchroute":
            return SearchRouteCommand(params, self._app_data)
        if cmd.lower() == "viewunassignedpackages":
            return ViewUnassignedPackages(params, self._app_data)
        if cmd.lower() == "viewpackageinfo":
            return ViewPackageInfo(params, self._app_data)
        if cmd.lower() == "assignpackage":
            return AssignPackage(params, self._app_data)

        raise InvalidCommand(cmd)


# should we handle the error? so it doesn't crash - probably
