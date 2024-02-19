import unittest
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.models_factory import ModelsFactory
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
            pass  # More code needed

    def test_ViewPackageInfo_command_whenNonEmpty(self):
        # Arrange
        models_factory = ModelsFactory()
        cmd_factory, app_data = test_setup()
        the_input = "viewpackageinfo 2"
        the_package = models_factory.create_package(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, 1.5,
                                                td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                                                td.VALID_PHONE_NUMBER, td.VALID_EMAIL)


        # Act
        app_data.add_package(the_package)
        package = app_data.find_package_by_id(1)
        command = cmd_factory.create(the_input)



        eta_str = (
            "not assigned yet" if package.eta is None else package.eta.strftime("%b %d %H:%M")
        )
        status_str = "not assigned yet" if package.status is None else package.status
        output = "\n".join(
            [
                f"ID: {1}",
                f"Weight: {1.5}",
                f"Destination: {"Melbourne"}",
                f"ETA: {eta_str}",
                f"Status: {status_str}",
                "-----contact info-----",
                f"Name: {"Alex"} {"Daskalov"}",
                f"Phone: {"1111111111"}",
                f"E-mail: {"AlexD@gmail.com"}",
            ]
        )

        # Assert
        self.assertEqual(app_data, command.app_data)
        if package is not None:
            self.assertEqual(package.display_info(), output)
