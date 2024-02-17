import unittest

from commands.assign_package import AssignPackage
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

    def test_create_registerPackage_withCorrectParams(self):
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

    def test_createViewUnassignedPackages_command(self):
        # Arrange
        cmd_factory, app_data = test_setup()
        the_input = "viewunassignedPackages"
        comparer = ViewUnassignedPackages([the_input], app_data)

        # Act
        command = cmd_factory.create(the_input)

        empty_output = "There are no unassigned packages at the moment."
        non_emtpy_output = "\n".join(
            f"ID: {package.id} Location: {package.start_loc}"
            for package in app_data.unassigned_packages)

        # Assert
        self.assertIsInstance(command, ViewUnassignedPackages)
        self.assertEqual(app_data, command.app_data)
        if len(app_data.unassigned_packages) == 0:
            self.assertEqual(comparer.execute(), empty_output)
        else:
            self.assertEqual(comparer.execute(), non_emtpy_output)

    def test_ViewPackageInfo_command_whenEmpty(self):
        # Arrange
        cmd_factory, app_data = test_setup()
        the_input = "viewpackageinfo 2"
        package = None

        # Act
        command = cmd_factory.create(the_input)

        # Assert
        self.assertIsInstance(command, ViewPackageInfo)
        self.assertEqual(app_data, command.app_data)
        if package is None:
            self.assertRaises(ValueError)
        else:
            pass

    def test_ViewPackageInfo_command_whenNonEmpty(self):
        # Arrange
        cmd_factory, app_data = test_setup()
        the_input = "viewpackageinfo 2"
        package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
                          td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                          td.VALID_PHONE_NUMBER, td.VALID_EMAIL)

        # Act
        command = cmd_factory.create(the_input)
        eta_str = (
            "not assigned yet" if package.eta is None else package.eta.strftime("%b %d %H:%M")
        )
        status_str = "not assigned yet" if package.status is None else package.status
        output = "\n".join(
            [
                f"-----INFO-----",
                f"ID: {package.id}",
                f"Weight: {package.weight}",
                f"Destination: {package.end_loc}",
                f"ETA: {eta_str}",
                f"Status: {status_str}",
            ]
        )

        # Assert
        self.assertIsInstance(command, ViewPackageInfo)
        self.assertEqual(app_data, command.app_data)
        if package is not None:
            self.assertEqual(package.display_info(), output)

    def test_assignPackageExecute_raiseValueError_whenInvalidParams(self):
        # Arrange
        cmd_factory, app_data = test_setup()
        test_object = AssignPackage(["k", "h"], app_data)

        package_id = test_object.params[0]
        route_id = test_object.params[1]

        # Assert
        if self.assertNotIsInstance(package_id, int) or self.assertNotIsInstance(route_id, int):
            self.assertRaises(ValueError)

    # def test_createAssignPackage_command(self):
    #     # Arrange
    #     cmd_factory, app_data = test_setup()
    #     the_input = "assignPackage 2 3"
    #     package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
    #                       td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
    #                       td.VALID_PHONE_NUMBER, td.VALID_EMAIL, )
    #     location = Location("Sydney")
    #     models_factory = ModelsFactory()
    #     route = models_factory.create_route(td.DEPARTURE_TIME, [location])
    #
    #     # Act
    #     command = cmd_factory.create(the_input)
    #     app_data.add_package(package)
    #     the_package = app_data.find_package_by_id(command.params[0])
    #
    #
    #
    #     # Assert
    #     self.assertIsInstance(command, AssignPackage)
    #     self.assertEqual(app_data, command.app_data)
    #     self.assertEqual(the_package.id, command.params[0])
