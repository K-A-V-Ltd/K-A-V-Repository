import unittest

from commands.assign_package import AssignPackage
from commands.assign_truck import AssignTruck
from commands.create_route import CreateRouteCommand
from commands.register_package import RegisterPackageCommand
from commands.search_route import SearchRouteCommand
from commands.validation_helpers import try_parse_int
from commands.view_pack_info import ViewPackageInfo
from commands.view_unassigned import ViewUnassignedPackages
from core import models_factory
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.models_factory import ModelsFactory
from errors.invalid_command import InvalidCommandError
from models.location import Location
from models.package import Package
import test_data as td


def test_setup():
    app_data = ApplicationData()
    cmd_factory = CommandFactory(app_data)

    return cmd_factory, app_data


class CommandFactoryShould(unittest.TestCase):
    def test_raiseError_invalidCommandName(self):
        # Arrange
        the_input = "info 1 2 3"
        cmd_factory, app_data = test_setup()

        # Act & Assert
        with self.assertRaises(InvalidCommandError):
            cmd_factory.create(the_input)

    def test_create_registerPackageCommand_withCorrectParams(self):
        # Arrange
        the_input = 'RegisterPackage Sydney Melbourne 10 Alex Daskalov 1111111111 alexdaskalov@gmail.com'
        cmd_factory, app_data = test_setup()
        command_result = ("Sydney", "Melbourne", "10", "Alex", "Daskalov", "1111111111", "alexdaskalov@gmail.com")

        # Act
        command = cmd_factory.create(the_input)

        # Assert
        self.assertIsInstance(command, RegisterPackageCommand)
        self.assertIsInstance(command.models_factory, ModelsFactory)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(command_result, command.params)

    def test_createRouteCommand_withCorrectParams(self):
        # Arrange
        the_input = "createRoute Mar 11 12:30 Sydney Brisbane Adelaide Perth"
        cmd_factory, app_data = test_setup()
        command_result = ("Mar", "11", "12:30", "Sydney", "Brisbane", "Adelaide", "Perth")

        # Act
        command = cmd_factory.create(the_input)

        # Assert
        self.assertIsInstance(command, CreateRouteCommand)
        self.assertIsInstance(command.models_factory, ModelsFactory)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(command_result, command.params)

    def test_createSearchRouteCommand_withCorrectParams(self):
        # Arrange
        the_input = "SearchRoute Sydney Perth"
        cmd_factory, app_data = test_setup()
        command_result = ("Sydney", "Perth")

        # Act
        command = cmd_factory.create(the_input)

        # Assert
        self.assertIsInstance(command, SearchRouteCommand)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(command_result, command.params)

    def test_createViewUnassignedPackagesCommand_withCorrectParams(self):
        # Arrange
        cmd_factory, app_data = test_setup()
        the_input = "viewunassignedpackages"


        # Act
        command = cmd_factory.create(the_input)

        # Assert
        self.assertIsInstance(command, ViewUnassignedPackages)
        self.assertEqual(app_data, command.app_data)


    def test_createViewPackageInfoCommand_withCorrectParams(self):
        # Arrange
        cmd_factory, app_data = test_setup()
        the_input = "viewpackageinfo 2"
        comparer = ('2',)

        # Act
        command = cmd_factory.create(the_input)

        # Assert
        self.assertIsInstance(command, ViewPackageInfo)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(comparer, command.params)

    def test_createAssignPackageCommand_withCorrectParams(self):
        # Arrange
        cmd_factory, app_data = test_setup()
        the_input = "assignPackage 2 3"
        comparer = ('2', '3')

        # Act
        command = cmd_factory.create(the_input)

        # Assert
        self.assertIsInstance(command, AssignPackage)
        self.assertEqual(app_data,command.app_data)
        self.assertEqual(comparer,command.params)

    def test_createAssignTruckCommand_withCorrectParams(self):
        # Arrange
        cmd_factory, app_data = test_setup()
        the_input = "assigntruck 1011"
        comparer = ("1011",)

        # Act
        command = cmd_factory.create(the_input)

        # Assert
        self.assertIsInstance(command, AssignTruck)
        self.assertEqual(app_data, command.app_data)
        self.assertEqual(comparer, command.params)



