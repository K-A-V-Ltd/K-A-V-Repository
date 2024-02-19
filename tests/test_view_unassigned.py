import unittest

from commands.view_unassigned import ViewUnassignedPackagesCommand
from core.application_data import ApplicationData
from core.command_factory import CommandFactory


def test_setup():
    app_data = ApplicationData()
    cmd_factory = CommandFactory(app_data)

    return cmd_factory, app_data


class ViewUnassignedPackagesShould(unittest.TestCase):

    def test_createViewUnassignedPackages(self):
        # Arrange
        cmd_factory, app_data = test_setup()
        the_input = "viewunassignedPackages"
        comparer = ViewUnassignedPackagesCommand([the_input], app_data)

        # Act
        empty_output = "There are no unassigned packages at the moment."
        non_emtpy_output = "\n".join(
            f"ID: {package.id} Location: {package.start_loc}"
            for package in app_data.unassigned_packages)

        # Assert
        if len(app_data.unassigned_packages) == 0:
            self.assertEqual(comparer.execute(), empty_output)
        else:
            self.assertEqual(comparer.execute(), non_emtpy_output)
