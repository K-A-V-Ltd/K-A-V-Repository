import unittest

from core.models_factory import ModelsFactory
import test_data as td
from models.location import Location
from models.package import Package
from models.route import Route


class ModelsFactoryShould(unittest.TestCase):
    def test_createValidRouteInstance(self):
        # Arrange
        models_factory = ModelsFactory()
        location = Location("Sydney")

        # Act
        route = models_factory.create_route(td.DEPARTURE_TIME, [location])

        # Assert
        self.assertIsInstance(route, Route)
        self.assertEqual(1, route.id)
        self.assertEqual((location,), route.locations)

    def test_createRoutesWithConsecutiveIds(self):
        # Arrange
        models_factory = ModelsFactory()
        location = Location("Sydney")

        # Act
        route = models_factory.create_route(td.DEPARTURE_TIME, [location])
        route1 = models_factory.create_route(td.DEPARTURE_TIME, [location])

        # Assert
        self.assertEqual(1, route.id)
        self.assertEqual(2, route1.id)

    def test_createValidPackageInstance(self):
        # Arrange
        models_factory = ModelsFactory()

        # Act
        package = models_factory.create_package(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 1.5,
                                                td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                                                td.VALID_PHONE_NUMBER, td.VALID_EMAIL)

        # Assert
        self.assertIsInstance(package, Package)
        self.assertEqual(1, package.id)

    def test_createPackagesWithConsecutiveIds(self):
        # Arrange
        models_factory = ModelsFactory()

        # Act
        package = models_factory.create_package(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 1.5,
                                                td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                                                td.VALID_PHONE_NUMBER, td.VALID_EMAIL)
        package1 = models_factory.create_package(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 1.5,
                                                 td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                                                 td.VALID_PHONE_NUMBER, td.VALID_EMAIL)

        # Assert
        self.assertEqual(1, package.id)
        self.assertEqual(2, package1.id)
