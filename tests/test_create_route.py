import unittest
from commands.base.base_command import BaseCommand
from commands.create_route import CreateRouteCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from errors.invalid_minimum_params import InvalidMinimumParams



class CreateRouteShould(unittest.TestCase):
    def test_initializerRaisesError_whenParamsNotEnough(self):
        APP_DATA = ApplicationData()
        MDL_FACTORY = ModelsFactory()
        with self.assertRaises(InvalidMinimumParams):
            tst_command = CreateRouteCommand([str(i) for i in range(4)], APP_DATA, MDL_FACTORY)

    def test_initializerSetsAttributes_whenParamsAreEnough(self):
        APP_DATA = ApplicationData()
        MDL_FACTORY = ModelsFactory()
        tst_command = CreateRouteCommand([str(i) for i in range(5)], APP_DATA, MDL_FACTORY)
        self.assertIsInstance(tst_command, CreateRouteCommand)

    def test_createSucessfullyCreatesRoute_whenParamsAreEnough(self):
        APP_DATA = ApplicationData()
        MDL_FACTORY = ModelsFactory()
        tst_command = CreateRouteCommand(["Feb", "24", "12:00", "Brisbane", "Adelaide"], APP_DATA, MDL_FACTORY)
        create_run = tst_command.execute()
        self.assertEqual("Route with ID: 1 and departure time: 2024-02-24 12:00:00 created.", create_run)

    def test_createRaisesValueError_whenMonthDateOrTimeNotValid(self):
        APP_DATA = ApplicationData()
        MDL_FACTORY = ModelsFactory()
        tst_command = CreateRouteCommand(["Lol", "lol", "lol", "Brisbane", "Adelaide"], APP_DATA, MDL_FACTORY)
        create_run = tst_command.execute()
        self.assertEqual("ValueError: time data 'Lol lol lol' does not match format '%b %d %H:%M'", create_run)

    def test_createRaisesCustomError_whenLocationsNotValid(self):
        APP_DATA = ApplicationData()
        MDL_FACTORY = ModelsFactory()
        tst_command = CreateRouteCommand(["Feb", "24", "12:00", "Sofia", "Varna"], APP_DATA, MDL_FACTORY)
        create_run = tst_command.execute()
        self.assertEqual("InvalidLocationError: 'Sofia' is not a valid location.", create_run)
