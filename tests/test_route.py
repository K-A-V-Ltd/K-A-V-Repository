import unittest
from models.route import Route
from models.locs_distance import Locations
from models.location import Location
from models.package import Package
from models.vehicles.trucks_creation import Garage
from models.vehicles.vehicle import Vehicle
from datetime import datetime, timedelta
import utils.time_abstraction as abstraction


class RouteShould(unittest.TestCase):
    def test_initializerSetsAttributes_whenCalled(self):
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        start = datetime.strptime("Mar 1 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2])
        self.assertIsInstance(tst_route._id, int)
        self.assertIsInstance(tst_route._departure_time, datetime)
        self.assertIsInstance(tst_route._locations, list)
        self.assertIsNone(tst_route.truck)

    def test_locationsProperty_returnsTuple(self):
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        start = datetime.strptime("Mar 1 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2])
        self.assertIsInstance(tst_route.locations, tuple)

    def test_truckPropertySetter_changesValueOfTruckProprty(self):
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        start = datetime.strptime("Mar 1 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2])
        truck1 = Garage[0]
        tst_route.truck = truck1
        self.assertIsInstance(tst_route.truck, Vehicle)

    def test_statusPropertyReturnsProperStatus_whenTheTravelIsWaitingToStart(self):
        abstraction.my_current_time = datetime.strptime("Feb 23 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        loc3 = Location("Sydney")
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2, loc3, loc2, loc1])
        truck1 = Garage[0]
        tst_route.truck = truck1
        expected = "waiting to start"
        self.assertEqual(expected, tst_route.status)

    def test_statusPropertyReturnsProperStatus_whenTheTravelHasFinished(self):
        abstraction.my_current_time = datetime.strptime("Mar 30 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        loc3 = Location("Sydney")
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2, loc3, loc2, loc1])
        truck1 = Garage[0]
        tst_route.truck = truck1
        expected = "finished"
        self.assertEqual(expected, tst_route.status)

    def test_statusPropertyReturnsProperStatus_whenTheTravelIsInProgress(self):
        abstraction.my_current_time = datetime.strptime("Feb 26 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        loc3 = Location("Sydney")
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2, loc3, loc2, loc1])
        truck1 = Garage[0]
        tst_route.truck = truck1
        expected = "in progress"
        self.assertEqual(expected, tst_route.status)

    def test_totalDistanceProperty_returnsProperDistance(self):
        abstraction.my_current_time = datetime.strptime("Feb 23 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2])
        truck1 = Garage[0]
        tst_route.truck = truck1
        expected = 4311
        self.assertEqual(expected, tst_route.total_distance)

    def test_totalWeightPropertyReturnsProperValue_withLocationWeights(self):
        abstraction.my_current_time = datetime.strptime("Feb 23 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc1.weight = 500
        loc2 = Location("Perth")
        loc2.weight = 300
        loc3 = Location("Sydney")
        loc3.weight = 200
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2, loc3])
        truck1 = Garage[0]
        tst_route.truck = truck1
        self.assertEqual(1000, tst_route.total_weight)

    def test_totalWeightPropertyReturnsProperValue_whenLocationsHaveZeroWeight(self):
        abstraction.my_current_time = datetime.strptime("Feb 23 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc1.weight = 0
        loc2 = Location("Perth")
        loc2.weight = 0
        loc3 = Location("Sydney")
        loc3.weight = 0
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2, loc3])
        truck1 = Garage[0]
        tst_route.truck = truck1
        self.assertEqual(0, tst_route.total_weight)

    def test_totalTimeProperty_returnsProperTime(self):
        abstraction.my_current_time = datetime.strptime("Feb 23 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        loc3 = Location("Sydney")
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2, loc3])
        truck1 = Garage[0]
        tst_route.truck = truck1
        expected = (start, loc3.eta)
        self.assertEqual(expected, tst_route.total_time)

    def test_nextStopPropertyReturnsProperStop_whenTheTravelIsInProgress(self):
        abstraction.my_current_time = datetime.strptime("Feb 25 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        loc3 = Location("Sydney")
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2, loc3, loc2, loc1])
        truck1 = Garage[0]
        tst_route.truck = truck1
        expected = "Sydney"
        self.assertEqual(expected, tst_route.next_stop.name)

    def test_nextStopPropertyReturnsProperStop_whenTheTravelIsWaitingToStart(self):
        abstraction.my_current_time = datetime.strptime("Feb 20 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        loc3 = Location("Sydney")
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2, loc3])
        truck1 = Garage[0]
        tst_route.truck = truck1
        expected = "Brisbane"
        self.assertEqual(expected, tst_route.next_stop.name)

    def test_deliveryWeightPropertyReturnsProperWeight_whenTheTravelIsInProgress(self):
        abstraction.my_current_time = datetime.strptime("Feb 26 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc1.weight = 500
        loc2 = Location("Perth")
        loc2.weight = 500
        loc3 = Location("Sydney")
        loc3.weight = 500
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2, loc3, loc2, loc1])
        truck1 = Garage[0]
        tst_route.truck = truck1
        expected = 1000
        self.assertEqual(expected, tst_route.delivery_weight)

    def test_calculateEtaMethod_calculatesEtaForEachLocation(self):
        abstraction.my_current_time = datetime.strptime("Feb 20 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        loc3 = Location("Sydney")
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2, loc3])
        truck1 = Garage[0]
        tst_route.truck = truck1
        self.assertIsInstance(tst_route.locations[0].eta, datetime)
        self.assertIsInstance(tst_route.locations[1].eta, datetime)
        self.assertIsInstance(tst_route.locations[2].eta, datetime)

    def test_isValidPackageMethodReturnsTrue_whenValidPackage(self):
        abstraction.my_current_time = datetime.strptime("Feb 20 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        loc3 = Location("Sydney")
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2, loc3])
        truck1 = Garage[0]
        tst_route.truck = truck1
        pack = Package(1, "Brisbane", "Perth", 21, "Pesho", "Ivanov", "0888888888", "pesho@gmail.com")
        self.assertTrue(tst_route.is_valid_for_package(pack.start_loc, pack.end_loc))

    def test_isValidPackageMethodReturnsFalse_whenPackageHasSameLocationsInWrongOrder(self):
        abstraction.my_current_time = datetime.strptime("Feb 20 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        loc3 = Location("Sydney")
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2, loc3])
        truck1 = Garage[0]
        tst_route.truck = truck1
        pack = Package(1, "Perth", "Brisbane", 21, "Pesho", "Ivanov", "0888888888", "pesho@gmail.com")
        self.assertFalse(tst_route.is_valid_for_package(pack.start_loc, pack.end_loc))

    def test_isValidPackageMethodReturnsFalse_whenPackageHasDifferentLocations(self):
        abstraction.my_current_time = datetime.strptime("Feb 20 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        loc3 = Location("Sydney")
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2, loc3])
        truck1 = Garage[0]
        tst_route.truck = truck1
        pack = Package(1, "Adelaide", "Darwin", 21, "Pesho", "Ivanov", "0888888888", "pesho@gmail.com")
        self.assertFalse(tst_route.is_valid_for_package(pack.start_loc, pack.end_loc))

    def test_addPackageMethodAddsPackage_whenPackageEndLocation_includedInRouteLocations(self):
        abstraction.my_current_time = datetime.strptime("Feb 20 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        loc3 = Location("Sydney")
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2, loc3])
        truck1 = Garage[0]
        tst_route.truck = truck1
        pack = Package(1, "Brisbane", "Perth", 21, "Pesho", "Ivanov", "0888888888", "pesho@gmail.com")
        tst_route.add_package(pack)
        self.assertEqual(1, len(tst_route.locations[1].packages))

    def test_addPackageMethodDoesNotAddPackage_whenPackageEndLocation_notIncludedInRouteLocations(self):
        abstraction.my_current_time = datetime.strptime("Feb 20 12:00", "%b %d %H:%M")
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        loc3 = Location("Sydney")
        start = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        tst_route = Route(1, start, [loc1, loc2, loc3])
        truck1 = Garage[0]
        tst_route.truck = truck1
        pack = Package(1, "Brisbane", "Adelaide", 21, "Pesho", "Ivanov", "0888888888", "pesho@gmail.com")
        tst_route.add_package(pack)
        self.assertEqual(0, len(tst_route.locations[0].packages))
        self.assertEqual(0, len(tst_route.locations[1].packages))
        self.assertEqual(0, len(tst_route.locations[2].packages))
