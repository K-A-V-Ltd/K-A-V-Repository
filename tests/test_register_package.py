import unittest

from commands.register_package import RegisterPackageCommand
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.models_factory import ModelsFactory


def test_setup():
    app_data = ApplicationData()
    cmd_factory = CommandFactory(app_data)

    return cmd_factory, app_data


class RegisterPackageCommandShould(unittest.TestCase):
    def test_registerPackageExecute_raiseValueError_whenInvalidParams(self):
        # Arrange
        models_factory = ModelsFactory()
        cmd_factory, app_data = test_setup()
        test_object = RegisterPackageCommand(["k", "h", "35", "Alex", "Daskalov", '1111111111', 'AlexD@gmail.com'],
                                             app_data, models_factory)

        # Act
        start_loc = test_object.params[0]
        end_loc = test_object.params[1]
        weight = test_object.params[2]

        # Assert
        if (self.assertNotIsInstance(start_loc, int) or
                self.assertNotIsInstance(end_loc, int) or self.assertNotIsInstance(weight, int)):
            self.assertRaises(ValueError)

    def test_RegisterPackageExecute_whenValidParams(self):
        models_factory = ModelsFactory()
        cmd_factory, app_data = test_setup()
        the_input = "registerPackage Sydney Brisbane 23.5 John Scott 0386574856 john.dutton@gmail.com"
        package = models_factory.create_package("Sydney", "Brisbane", 23.5, "John", "Scott",
                                                "0386574856", "john.dutton@gmail.com")

        # Act
        command = cmd_factory.create(the_input)
        app_data.add_package(package)

        # Assert
        self.assertEqual(command.execute(), "Package #1 successfully registered.")
