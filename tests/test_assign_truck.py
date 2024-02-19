import unittest

from commands.assign_truck import AssignTruck
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.models_factory import ModelsFactory
from models.location import Location
import test_data as td
from models.package import Package


def test_setup():
    app_data = ApplicationData()
    cmd_factory = CommandFactory(app_data)

    return cmd_factory, app_data


class AssignTruckShould(unittest.TestCase):
    def test_assignTruckExecuteMethod_raiseValueError_whenInvalidParams(self):
        # Arrange
        cmd_factory, app_data = test_setup()
        test_object = AssignTruck(["k"], app_data)

        # Act
        route_id = test_object.params[0]

        # Assert
        if self.assertNotIsInstance(route_id, int):
            self.assertRaises(ValueError)

    def test_assignPackageExecuteMethod_when_TruckIsNotNone(self):
        # Arrange
        models_factory = ModelsFactory()
        cmd_factory, app_data, = test_setup()
        location = Location("Sydney")
        package = td.VALID_PACKAGE
        route_object = models_factory.create_route(td.DEPARTURE_TIME, [location])

        # Act
        command = cmd_factory.create("AssignTruck 1")
        app_data.add_route(route_object)
        location.add_package(package)


        route = app_data.find_route_by_id(route_object.id)
        truck = app_data.find_suitable_truck(route)
        truck.add_route(route)

        # Assert
        self.assertEqual(command.execute(), f"Truck #1002 successfully assigned to route #1")

    def test_assignPackageExecuteMethod_when_TruckIsNone(self):
        models_factory = ModelsFactory()
        cmd_factory, app_data, = test_setup()
        location = Location("Sydney")
        the_input = "AssignTruck 1"
        package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 1111111111111,
                          td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                          td.VALID_PHONE_NUMBER, td.VALID_EMAIL)
        route_object = models_factory.create_route(td.DEPARTURE_TIME, [location])

        # Act
        command = cmd_factory.create(the_input)

        app_data.add_route(route_object)
        location.add_package(package)
        route = app_data.find_route_by_id(1)
        truck = app_data.find_suitable_truck(route)

        # Assert
        self.assertEqual(command.execute(), "There are no suitable available trucks at the moment.")


