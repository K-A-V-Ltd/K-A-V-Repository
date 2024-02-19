import unittest
from models.package import Package
from models.location import Location
from datetime import datetime


class LocationShould(unittest.TestCase):
    def test_initializerSetsAttributes_whenCalled(self):
        loc = Location("Brisbane")
        self.assertIsInstance(loc._name, str)
        self.assertIsInstance(loc.weight, int)
        self.assertIsInstance(loc.packages, list)
        self.assertIsNone(loc.eta)

    def test_etaPropertySetter_changesValueOfEtaProperty(self):
        loc = Location("Brisbane")
        eta1 = loc.eta
        loc.eta = datetime.now()
        self.assertNotEqual(eta1, loc.eta)

    def test_weightPropertySetter_changesValueOfWeightProperty(self):
        loc = Location("Brisbane")
        weight1 = loc.weight
        loc.weight = 100
        self.assertNotEqual(weight1, loc.eta)

    def test_addPackage_addsPackageToPackages(self):
        loc = Location("Brisbane")
        pack = Package(1, "Brisbane", "Perth", 21, "Pesho", "Ivanov", "0888888888", "pesho@gmail.com")
        loc.add_package(pack)
        self.assertEqual(1, len(loc.packages))

    def test_removePackage_removesExistingPackageFromPackages(self):
        loc = Location("Brisbane")
        pack = Package(1, "Brisbane", "Perth", 21, "Pesho", "Ivanov", "0888888888", "pesho@gmail.com")
        loc.add_package(pack)
        loc.remove_package(pack)
        self.assertEqual(0, len(loc.packages))
