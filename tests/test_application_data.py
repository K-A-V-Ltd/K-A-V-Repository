import unittest
from core.application_data import ApplicationData
from models.package import Package
from models.route import Route
from datetime import datetime
from models.vehicles.trucks_creation import Garage
from models.vehicles.vehicle import Vehicle
from models.location import Location


class ApplicationDataShould(unittest.TestCase):
    def test_initializerSetsAttributes_whenCalled(self):
        APP_DATA = ApplicationData()
        self.assertIsInstance(APP_DATA.unassigned_packages, list)
        self.assertIsInstance(APP_DATA.all_packages, list)
        self.assertIsInstance(APP_DATA.routes, list)
        self.assertIsInstance(APP_DATA._garage, list)

    def test_addPackage_addsPackageToUnassignedPackages(self):
        APP_DATA = ApplicationData()
        pack = Package(1, "Brisbane", "Perth", 21, "Pesho", "Ivanov", "0888888888", "pesho@gmail.com")
        APP_DATA.add_package(pack)
        self.assertEqual(APP_DATA.unassigned_packages[0], pack)

    def test_addPackage_addsPackageToAllPackages(self):
        APP_DATA = ApplicationData()
        pack = Package(1, "Brisbane", "Perth", 21, "Pesho", "Ivanov", "0888888888", "pesho@gmail.com")
        APP_DATA.add_package(pack)
        self.assertEqual(APP_DATA.all_packages[0], pack)

    def test_addRoute_addsRouteToRoutes(self):
        APP_DATA = ApplicationData()
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        route = Route(1, datetime.now(), [loc1, loc2])
        APP_DATA.add_route(route)
        self.assertEqual(APP_DATA.routes[0], route)

    def test_findSuitableRoute_findsSuitableRoutes_whenRoutesAvailable(self):
        APP_DATA = ApplicationData()
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        route = Route(1, datetime.now(), [loc1, loc2])
        APP_DATA.add_route(route)
        suitable = APP_DATA.find_suitable_route("Brisbane", "Perth")
        self.assertEqual(suitable[0], route)

    def test_findSuitableRoute_doesNotFindSuitableRoutes_whenNoSuitableRoutesAreAvailable(self):
        APP_DATA = ApplicationData()
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        route = Route(1, datetime.now(), [loc1, loc2])
        APP_DATA.add_route(route)
        suitable = APP_DATA.find_suitable_route("Sydney", "Adelaide")
        self.assertEqual(0, len(suitable))

    def test_findSuitableTruck_findsSuitableTruck_whenTruckAvailable(self):
        APP_DATA = ApplicationData()
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        route = Route(1, datetime.now(), [loc1, loc2])
        APP_DATA.add_route(route)
        self.assertIsInstance(APP_DATA.find_suitable_truck(route), Vehicle)

    def test_findSuitableTruck_doesNotFindSuitableTruck_whenNoSuitableTruckAvailable(self):
        APP_DATA = ApplicationData()
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        route = Route(1, datetime.now(), [loc1, loc2])
        APP_DATA.add_route(route)
        APP_DATA._garage = []
        self.assertEqual(None, APP_DATA.find_suitable_truck(route))

    def test_findRouteById_findsRoute_whenRouteWithSuchIdExists(self):
        APP_DATA = ApplicationData()
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        route = Route(1, datetime.now(), [loc1, loc2])
        APP_DATA.add_route(route)
        self.assertIsInstance(APP_DATA.find_route_by_id(1), Route)

    def test_findRouteById_doesNotFindRoute_whenRouteWithSuchIdDoesNotExist(self):
        APP_DATA = ApplicationData()
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        route = Route(1, datetime.now(), [loc1, loc2])
        APP_DATA.add_route(route)
        self.assertEqual(None, APP_DATA.find_route_by_id(2))

    def test_findPackageById_findsPackage_whenPackageWithSuchIdExists(self):
        APP_DATA = ApplicationData()
        pack = Package(1, "Brisbane", "Perth", 21, "Pesho", "Ivanov", "0888888888", "pesho@gmail.com")
        APP_DATA.add_package(pack)
        self.assertIsInstance(APP_DATA.find_package_by_id(1), Package)

    def test_findPackageById_doesNotFindPackage_whenPackageWithSuchIdDoesNotExist(self):
        APP_DATA = ApplicationData()
        pack = Package(1, "Brisbane", "Perth", 21, "Pesho", "Ivanov", "0888888888", "pesho@gmail.com")
        APP_DATA.add_package(pack)
        self.assertEqual(None, APP_DATA.find_package_by_id(2))


# class ApplicationDataShould(unittest.TestCase):
#     def test_assignCollections(self):
#         # Arrange & Act
#         app_data = ApplicationData()
#
#         # Assert
#         self.assertEqual([], app_data.all_packages)
#         self.assertEqual([], app_data.routes)
#
#     def test_successfulInsertion_ofPackage(self):
#         # Arrange
#         app_data = ApplicationData()
#         package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
#                           td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
#                           td.VALID_PHONE_NUMBER, td.VALID_EMAIL, )
#
#         # Act
#         app_data.add_package(package)
#
#         # Assert
#         self.assertIn(package, app_data.all_packages)
#
#     def test_raiseError_whenAttempting_toAddNone_asPackage(self):
#         app_data = ApplicationData()
#         package = None
#
#         # Act & Assert
#         with self.assertRaises(ValueError):
#             app_data.add_package(package)
#
#     def test_successfulInsertion_ofRoute(self):
#         # Arrange
#         app_data = ApplicationData()
#         route = Route(1, td.DEPARTURE_TIME, td.LOCATIONS)
#
#         # Act
#         app_data.add_route(route)
#
#         # Assert
#         self.assertIn(route, app_data.routes)
#
#     def test_raiseError_whenAttempting_toAddNone_asRoute(self):
#         app_data = ApplicationData()
#         route = None
#
#         # Act & Assert
#         with self.assertRaises(ValueError):
#             app_data.add_package(route)
#
#     def test_findRoute_byId_returnsRoute_whenExists(self):
#         app_data = ApplicationData()
#         route = Route(1, td.DEPARTURE_TIME, td.LOCATIONS)
#
#         # Act
#         app_data.add_route(route)
#
#         # Assert
#         self.assertEqual(route, app_data.find_route_by_id(1))
#
#     def test_findRoute_byId_returnsNone_whenDoesntExist(self):
#         app_data = ApplicationData()
#         route = Route(1, td.DEPARTURE_TIME, td.LOCATIONS)
#
#         # Act
#         app_data.add_route(route)
#
#         # Assert
#         self.assertEqual(None, app_data.find_route_by_id(2))
#
#     # def test_DisplayThePackagesContent(self):
#     #     # Arrange
#     #     app_data = ApplicationData()
#     #     package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
#     #                       td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
#     #                       td.VALID_PHONE_NUMBER, td.VALID_EMAIL)
#     #     def testPrint():
#     #         for x in app_data._packages:
#     #             print(x.weight)
#     #
#     #
#     #     # Act
#     #     result = app_data.add_package(package)
#     #
#     #     # Assert
#     #     self.assertEqual(app_data.display_packs(), package.weight)
#
#     # def test_findSuitableRoute_returnsSuccessfully(self):
#     #     # Arrange
#     #     app_data = ApplicationData()
#     #     package = Package(1, td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION, td.VALID_PACKAGE,
#     #                       td.VALID_FIRST_NAME, td.VALID_LAST_NAME,
#     #                       td.VALID_PHONE_NUMBER, td.VALID_EMAIL)
#     #     route = Route(1, td.DEPARTURE_TIME, td.LOCATIONS)
#     #     result = app_data.find_suitable_route(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION)
#     #
#     #     # Act
#     #     app_data.add_package(package)
#     #     app_data.add_route(route)
#     #
#     #     # Assert
#     #     self.assertEqual(result, td.LOCATIONS)
#
#     def test_findSuitableRoute_returnsEmptyList_whenNoSuitableRoutes(self):
#         # Arrange
#         app_data = ApplicationData()
#
#         # Act
#         result = app_data.find_suitable_route(td.VALID_STARTING_LOCATION, td.VALID_ENDING_LOCATION)
#
#
#         # Assert
#         self.assertEqual(result, [])
