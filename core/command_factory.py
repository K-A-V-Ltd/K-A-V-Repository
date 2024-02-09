from commands.register_package import RegisterPackageCommand
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

        raise InvalidCommand(cmd)
