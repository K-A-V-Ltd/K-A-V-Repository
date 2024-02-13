import unittest

from models.package import Package
import test_data as td


class PackageShould(unittest.TestCase):
    def test_validDataTypes(self):
        # Arrange & Act
        object_for_testing = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
                                     td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                                     td.VALID_PHONE_NUMBER, td.VALID_EMAIL)
        # Assert
        self.assertIsInstance(object_for_testing.start_loc, str)
        self.assertIsInstance(object_for_testing.end_loc, str)
        self.assertIsInstance(object_for_testing.weight, float)
        self.assertIsInstance(object_for_testing.last_name, str)
        self.assertIsInstance(object_for_testing.first_name, str)
        self.assertIsInstance(object_for_testing.phone_number, str)
        self.assertIsInstance(object_for_testing.email, str)

    def test_init_raiseError_firstNameInvalid(self):
        with self.assertRaises(ValueError):
            Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE, "", td.VALID_LAST_NAME,
                    td.VALID_PHONE_NUMBER, td.VALID_EMAIL, )

    def test_init_raiseError_lastNameInvalid(self):
        with self.assertRaises(ValueError):
            Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE, td.VALID_FIRST_NAME, "",
                    td.VALID_PHONE_NUMBER, td.VALID_EMAIL)

    def test_init_raiseError_EmailInvalid(self):
        with self.assertRaises(ValueError):
            Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE, td.VALID_FIRST_NAME,
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
        object_for_testing = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
                                     td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                                     td.VALID_PHONE_NUMBER, td.VALID_EMAIL, )
        expected_output = (f"Package with weight: {td.VALID_PACKAGE}\n"
                           f"Sent from: {td.VALID_STARTING_LOCATION}\n"
                           f"Sent to: {td.VALID_ENDING_LOCATION}\n"
                           f"Sent by: {td.VALID_FIRST_NAME} {td.VALID_LAST_NAME}\n"
                           f"Sender contact information: {td.VALID_EMAIL} Phone number: {td.VALID_PHONE_NUMBER}\n")

        # Act
        stringed_object = str(object_for_testing)

        # Assert
        self.assertEqual(expected_output, stringed_object)
