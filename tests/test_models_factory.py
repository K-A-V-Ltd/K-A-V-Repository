import unittest

from core.models_factory import ModelsFactory
import test_data as td
from models.package import Package
from models.route import Route


class ModelsFactoryShould(unittest.TestCase):
    def test_createValidRouteInstance(self):
        # Arrange
        models_factory = ModelsFactory()
        departure_time = td.DEPARTURE_TIME
        locations = []

        # Act
        test = models_factory.create_route(departure_time, locations)

        # Assert
        self.assertIsInstance(test,Route)
        self.assertEqual(1, test.id)
        self.assertEqual((), test.locations)

    def test_createRoutesWithConsecutiveIds(self):
        # Arrange
        models_factory = ModelsFactory()
        departure_time = td.DEPARTURE_TIME
        locations = []

        # Act
        test = models_factory.create_route(departure_time, locations)
        test1 = models_factory.create_route(departure_time, locations)


        # Assert
        self.assertEqual(1, test.id)
        self.assertEqual(2, test1.id)


    def test_createValidPackageInstance(self):
        # Arrange
        models_factory = ModelsFactory()

        # Act
        package = models_factory.create_package(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE, td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                    td.VALID_PHONE_NUMBER, td.VALID_EMAIL)

        # Assert
        self.assertIsInstance(package, Package)
        self.assertEqual(1,package.id)

    def test_createPackagesWithConsecutiveIds(self):
        # Arrange
        models_factory = ModelsFactory()

        # Act
        package = models_factory.create_package(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
                                                td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                                                td.VALID_PHONE_NUMBER, td.VALID_EMAIL)
        package1 = models_factory.create_package(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
                                                td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                                                td.VALID_PHONE_NUMBER, td.VALID_EMAIL)

        # Assert
        self.assertEqual(1, package.id)
        self.assertEqual(2, package1.id)











