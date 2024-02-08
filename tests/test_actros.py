import unittest
import test_data as td
from custom_errors import OwnedVehicles
from models.vehicles.actros import Actros
from models.package import Package


class ActrosShould(unittest.TestCase):
    def test_validDataTypes(self):
        # Arrange
        object_actros = Actros(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION)

        # Act & Assert
        self.assertIsInstance(object_actros.ending_location, str)
        self.assertIsInstance(object_actros.starting_location, str)
        self.assertIsInstance(object_actros.packages, list)

    def test_addPackage_method(self):
        # Arrange
        object_actros = Actros(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION)
        package = Package(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE, td.VALID_FIRST_NAME,
                          td.VALID_LAST_NAME, td.VALID_PHONE_NUMBER, td.VALID_EMAIL)

        # Act
        object_actros.add_package(package)

        # Assert
        self.assertIn(package, object_actros.packages)

    def test_addPackage_raisesError_ifNone(self):
        # Arrange
        object_actros = Actros(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION)
        package = None

        # Act & Assert
        with self.assertRaises(ValueError):
            object_actros.add_package(package)

    def test_removePackage_method(self):
        # Arrange
        object_actros = Actros(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION)
        package = Package(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE, td.VALID_FIRST_NAME,
                          td.VALID_LAST_NAME, td.VALID_PHONE_NUMBER, td.VALID_EMAIL)

        # Act
        object_actros.add_package(package)
        object_actros.remove_package(package)

        # Assert
        self.assertNotIn(package, object_actros.packages)

    def test_removePackage_raisesError_ifNonExistent(self):
        # Arrange
        object_actros = Actros(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION)
        package = Package(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE, td.VALID_FIRST_NAME,
                          td.VALID_LAST_NAME, td.VALID_PHONE_NUMBER, td.VALID_EMAIL)

        # Act & Assert
        with self.assertRaises(ValueError):
            object_actros.remove_package(package)

    def test_successfulPrevention_of_creatingMoreTrucks_ofTypeActros(self):
        for _ in range(14):
            Actros(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION)

        # & Assert
        with self.assertRaises(OwnedVehicles):
            Actros(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION)
