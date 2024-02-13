import unittest
import test_data as td
from errors.vehicles_limit import OwnedVehicles
from models.vehicles.man import Man
from models.package import Package


class ManShould(unittest.TestCase):
    def test_validDataTypes(self):
        # Arrange
        object_actros = Man()

        # Act & Assert
        self.assertIsInstance(object_actros.packages, list)

    def test_addPackage_method(self):
        # Arrange
        object_actros = Man()
        package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
                          td.VALID_FIRST_NAME,
                          td.VALID_LAST_NAME, td.VALID_PHONE_NUMBER, td.VALID_EMAIL)

        # Act
        object_actros.add_package(package)

        # Assert
        self.assertIn(package, object_actros.packages)

    def test_addPackage_raisesError_ifNone(self):
        # Arrange
        object_actros = Man()
        package = None

        # Act & Assert
        with self.assertRaises(ValueError):
            object_actros.add_package(package)

    def test_removePackage_method(self):
        # Arrange
        object_actros = Man()
        package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
                          td.VALID_FIRST_NAME,
                          td.VALID_LAST_NAME, td.VALID_PHONE_NUMBER, td.VALID_EMAIL)

        # Act
        object_actros.add_package(package)
        object_actros.remove_package(package)

        # Assert
        self.assertNotIn(package, object_actros.packages)

    def test_removePackage_raisesError_ifNonExistent(self):
        # Arrange
        object_actros = Man()
        package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
                          td.VALID_FIRST_NAME,
                          td.VALID_LAST_NAME, td.VALID_PHONE_NUMBER, td.VALID_EMAIL)

        # Act & Assert
        with self.assertRaises(ValueError):
            object_actros.remove_package(package)

    def test_remainingCapacityReturnsSuccessfully(self):
        object_actros = Man()
        package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
                          td.VALID_FIRST_NAME, td.VALID_LAST_NAME, td.VALID_PHONE_NUMBER, td.VALID_EMAIL)

        object_actros.add_package(package)
        result = object_actros.weight - package.weight

        self.assertEqual(object_actros.unused_capacity, result)
