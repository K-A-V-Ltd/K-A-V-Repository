import unittest
from datetime import datetime

from core.application_data import ApplicationData
from models.package import Package
import test_data as td
from models.route import Route
from models.locs_distance import Locations


class ApplicationDataShould(unittest.TestCase):
    def test_assignCollections(self):
        # Arrange & Act
        app_data = ApplicationData()

        # Assert
        self.assertEqual([], app_data._packages)
        self.assertEqual([], app_data._routes)

    def test_successfulInsertion_ofPackage(self):
        # Arrange
        app_data = ApplicationData()
        package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
                          td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
                          td.VALID_PHONE_NUMBER, td.VALID_EMAIL, )

        # Act
        app_data.add_package(package)

        # Assert
        self.assertIn(package, app_data._packages)

    def test_raiseError_whenAttempting_toAddNone_asPackage(self):
        app_data = ApplicationData()
        package = None

        # Act & Assert
        with self.assertRaises(ValueError):
            app_data.add_package(package)

    def test_successfulInsertion_ofRoute(self):
        # Arrange
        app_data = ApplicationData()
        route = Route(1, td.DEPARTURE_TIME, td.LOCATIONS)

        # Act
        app_data.add_route(route)

        # Assert
        self.assertIn(route, app_data._routes)

    def test_raiseError_whenAttempting_toAddNone_asRoute(self):
        app_data = ApplicationData()
        route = None

        # Act & Assert
        with self.assertRaises(ValueError):
            app_data.add_package(route)

    def test_findRoute_byId_returnsRoute_whenExists(self):
        app_data = ApplicationData()
        route = Route(1, td.DEPARTURE_TIME, td.LOCATIONS)

        # Act
        app_data.add_route(route)

        # Assert
        self.assertEqual(route, app_data.find_route_by_id(1))

    def test_findRoute_byId_returnsNone_whenDoesntExist(self):
        app_data = ApplicationData()
        route = Route(1, td.DEPARTURE_TIME, td.LOCATIONS)

        # Act
        app_data.add_route(route)

        # Assert
        self.assertEqual(None, app_data.find_route_by_id(2))

    # def test_DisplayThePackagesContent(self):
    #     # Arrange
    #     app_data = ApplicationData()
    #     package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
    #                       td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
    #                       td.VALID_PHONE_NUMBER, td.VALID_EMAIL)
    #     def testPrint():
    #         for x in app_data._packages:
    #             print(x.weight)
    #
    #
    #     # Act
    #     result = app_data.add_package(package)
    #
    #     # Assert
    #     self.assertEqual(app_data.display_packs(), package.weight)

    # def test_findSuitableRoute_returnsSuccessfully(self):
    #     # Arrange
    #     app_data = ApplicationData()
    #     package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
    #                       td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
    #                       td.VALID_PHONE_NUMBER, td.VALID_EMAIL)
    #     route = Route(1, td.DEPARTURE_TIME, td.LOCATIONS)
    #     result = app_data.find_suitable_route(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION)
    #
    #     # Act
    #     app_data.add_package(package)
    #     app_data.add_route(route)
    #
    #     # Assert
    #     self.assertEqual(result, td.LOCATIONS)

    def test_findSuitableRoute_returnsEmptyList_whenNoSuitableRoutes(self):
        # Arrange
        app_data = ApplicationData()

        # Act
        result = app_data.find_suitable_route(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION)


        # Assert
        self.assertEqual(result, [])
