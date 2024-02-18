import unittest

from commands.view_pack_info import ViewPackageInfo
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from models.package import Package
import test_data as td


def test_setup():
    app_data = ApplicationData()
    cmd_factory = CommandFactory(app_data)

    return cmd_factory, app_data
class ViewPackageInfoShould(unittest.TestCase):
    def test_ViewPackageInfo_command_whenEmpty(self):
        # Arrange
        cmd_factory, app_data = test_setup()
        the_input = "viewpackageinfo 2"
        package = None

        # Act
        command = cmd_factory.create(the_input)

        # Assert
        self.assertEqual(app_data, command.app_data)
        if package is None:
            self.assertRaises(ValueError)
        else:
            pass # More code needed


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
        self.assertEqual(app_data, command.app_data)
        if package is not None:
            self.assertEqual(package.display_info(), output)