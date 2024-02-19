import unittest
from datetime import datetime

from models.package import Package
import test_data as td


class PackageShould(unittest.TestCase):
    def test_validDataTypes(self):
        # Arrange & Act
        package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 1.5,
                          td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                          td.VALID_PHONE_NUMBER, td.VALID_EMAIL)
        # Assert
        self.assertIsInstance(package.start_loc, str)
        self.assertIsInstance(package.end_loc, str)
        self.assertIsInstance(package.weight, float)
        self.assertIsInstance(package.last_name, str)
        self.assertIsInstance(package.first_name, str)
        self.assertIsInstance(package.phone_number, str)
        self.assertIsInstance(package.email, str)

    def test_validETA(self):
        # Arrange
        package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 1.5,
                          td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                          td.VALID_PHONE_NUMBER, td.VALID_EMAIL)
        # Act
        package.eta = td.DEPARTURE_TIME

        # Assert
        self.assertIsInstance(package.eta, datetime)

    def test_init_raiseError_firstNameInvalid(self):
        with self.assertRaises(ValueError):
            Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 1.5, "", td.VALID_LAST_NAME,
                    td.VALID_PHONE_NUMBER, td.VALID_EMAIL, )

    def test_init_raiseError_lastNameInvalid(self):
        with self.assertRaises(ValueError):
            Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 1.5, td.VALID_FIRST_NAME, "",
                    td.VALID_PHONE_NUMBER, td.VALID_EMAIL)

    def test_init_raiseError_EmailInvalid(self):
        with self.assertRaises(ValueError):
            Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 1.5, td.VALID_FIRST_NAME,
                    td.VALID_LAST_NAME,
                    td.VALID_PHONE_NUMBER, "")

    def test_init_raiseError_PackageInvalid(self):
        with self.assertRaises(ValueError):
            Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 0, td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                    td.VALID_PHONE_NUMBER, td.VALID_EMAIL, )

    def test_init_raiseError_phoneNumberInvalid(self):
        with self.assertRaises(ValueError):
            Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 0, td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                    "156", td.VALID_EMAIL, )

    def test_returnsCorrectly_when_strMethod_isValid(self):
        # Arrange
        package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 1.5,
                          td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                          td.VALID_PHONE_NUMBER, td.VALID_EMAIL, )
        expected_output = (f"Package with weight: {1.5}\n"
                           f"Sent from: {td.VALID_STARTING_LOCATION}\n"
                           f"Sent to: {td.VALID_ENDING_LOCATION}\n"
                           f"Sent by: {td.VALID_FIRST_NAME} {td.VALID_LAST_NAME}\n"
                           f"Sender contact information: {td.VALID_EMAIL} Phone number: {td.VALID_PHONE_NUMBER}\n")

        # Act
        stringed_object = str(package)

        # Assert
        self.assertEqual(expected_output, stringed_object)

    def test_displayInfo_returnsCorrectOutput(self):
        # Arrange
        package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 1.5,
                          td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                          td.VALID_PHONE_NUMBER, td.VALID_EMAIL, )

        # Act
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
        self.assertEqual(package.display_info(), output)
