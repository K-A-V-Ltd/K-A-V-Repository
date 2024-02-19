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
