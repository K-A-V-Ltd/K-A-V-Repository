import unittest

from commands.assign_package import AssignPackageCommand
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.models_factory import ModelsFactory
from models.location import Location
import test_data as td



def test_setup():
    app_data = ApplicationData()
    cmd_factory = CommandFactory(app_data)

    return cmd_factory, app_data


class AssignPackageCommandShould(unittest.TestCase):
    def test_assignPackageExecute_raiseValueError_whenInvalidParams(self):
        # Arrange
        cmd_factory, app_data = test_setup()
        test_object = AssignPackageCommand(["k", "h"], app_data)

        package_id = test_object.params[0]
        route_id = test_object.params[1]

        # Assert
        if self.assertNotIsInstance(package_id, int) or self.assertNotIsInstance(route_id, int):
            self.assertRaises(ValueError)

    def test_AssignPackageExecuteMethod_whenPackageIsNone(self):
        # Arrange
        cmd_factory, app_data, = test_setup()
        the_input = "assignPackage 2 3"

        # Act
        command = cmd_factory.create(the_input)

        # Assert
        self.assertEqual(command.execute(), "There is no such package in the system.")

    def test_AssignPackageExecuteMethod_whenRouteIsNone(self):
        # Arrange
        models_factory = ModelsFactory()
        cmd_factory, app_data, = test_setup()

        the_input = "assignPackage 1 1"

        # Act
        package = models_factory.create_package(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 1.5,
                                                td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                                                td.VALID_PHONE_NUMBER, td.VALID_EMAIL)
        command = cmd_factory.create(the_input)
        app_data.add_package(package)

        # Assert
        self.assertEqual(command.execute(), "There is no such route in the system.")

    def test_AssignPackageMethod_whenTruckCapacityReached(self):
        # Arrange
        models_factory = ModelsFactory()
        cmd_factory, app_data, = test_setup()

        the_input = "assignPackage 1 1"

        location = Location("Sydney")
        package = models_factory.create_package(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 99999999,
                                                td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                                                td.VALID_PHONE_NUMBER, td.VALID_EMAIL)
        route = models_factory.create_route(td.DEPARTURE_TIME, [location])

        # Act
        command = cmd_factory.create(the_input)
        app_data.add_package(package)
        app_data.add_route(route)
        route.truck = app_data._garage[0]

        # Assert
        self.assertEqual(command.execute(), "The truck assigned to this route has already reached its max capacity.")

    def test_AssignPackageMethod_successfulAssignment(self):
        # Arrange
        models_factory = ModelsFactory()
        cmd_factory, app_data, = test_setup()

        the_input = "assignPackage 1 1"

        location = Location("Sydney")
        package = models_factory.create_package(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 100,
                                                td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                                                td.VALID_PHONE_NUMBER, td.VALID_EMAIL)
        route = models_factory.create_route(td.DEPARTURE_TIME, [location])

        # Act
        command = cmd_factory.create(the_input)
        app_data.add_package(package)
        app_data.add_route(route)
        route.truck = app_data._garage[0]

        # Assert
        self.assertEqual(command.execute(), f"Package #{1} successfully assigned to route #{1}.")
