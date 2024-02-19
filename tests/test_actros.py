import unittest
import test_data as td
from core.models_factory import ModelsFactory
from models.location import Location
from models.vehicles.actros import Actros


class ActrosShould(unittest.TestCase):

    def test_validDataTypes(self):
        # Arrange
        object_actros = Actros()

        # Act & Assert
        self.assertEqual(object_actros.make, "Actros")
        self.assertIsInstance(object_actros.id, int)
        self.assertIsInstance(object_actros.weight_capacity, int)
        self.assertIsInstance(object_actros.range, int)
        self.assertIsInstance(object_actros.routes, tuple)

    def test_addRoute_appendsSuccessfully(self):
        # Arrange
        object_actros = Actros()
        models_factory = ModelsFactory()
        location = Location("Sydney")
        route = models_factory.create_route(td.DEPARTURE_TIME, [location])

        # Act
        object_actros.add_route(route)

        # Assert
        self.assertIn(route, object_actros.routes)

    def test_checkTimeOverlapReturnsTrue_whenItOverlaps(self):
        # Arrange
        object_actros = Actros()
        models_factory = ModelsFactory()
        location = Location("Sydney")

        # Act
        route1 = models_factory.create_route(td.DEPARTURE_TIME, [location])
        route2 = models_factory.create_route(td.DEPARTURE_TIME, [location])

        # Assert
        self.assertEqual(True, object_actros.check_time_overlap(route1, route2))

    def test_checkTimeOverlapReturnsFalse_whenDoesntOverlap(self):
        # Arrange
        object_actros = Actros()
        models_factory = ModelsFactory()
        location = Location("Sydney")
        location2 = Location("Perth")

        # Act
        route1 = models_factory.create_route(td.DEPARTURE_TIME, [location])
        route2 = models_factory.create_route(td.DEPARTURE_TIME2, [location2])

        # Assert
        self.assertEqual(False, object_actros.check_time_overlap(route1, route2))

    def test_overlapReturnsTrue_whenOverlaps(self):
        # Arrange
        object_actros = Actros()
        models_factory = ModelsFactory()
        location = Location("Sydney")

        # Act
        route = models_factory.create_route(td.DEPARTURE_TIME, [location])
        object_actros.add_route(route)
        new_route = models_factory.create_route(td.DEPARTURE_TIME, [location])

        # Assert
        self.assertEqual(True, object_actros.overlap(new_route))

    def test_overlapReturnsFalse_whenDoesntOverlap(self):
        # Arrange
        object_actros = Actros()
        models_factory = ModelsFactory()
        location = Location("Sydney")

        # Act
        new_route = models_factory.create_route(td.DEPARTURE_TIME, [location])

        # Assert
        self.assertEqual(False, object_actros.overlap(new_route))

    def test_isValidForRouteReturns_trueWhenValid(self):
        # Arrange
        object_actros = Actros()
        models_factory = ModelsFactory()
        location = Location("Sydney")

        # Act
        route = models_factory.create_route(td.DEPARTURE_TIME, [location])

        # Assert
        self.assertEqual(True, object_actros.is_valid_for_route(route))

    def test_isValidForRouteReturns_falseWhenInvalid(self):
        # Arrange
        object_actros = Actros()
        models_factory = ModelsFactory()
        location = Location("Sydney")
        location.weight = 11111111111111111111111  # kg  (Big package ^^)

        # Act
        route = models_factory.create_route(td.DEPARTURE_TIME, [location])

        # Assert
        self.assertEqual(False, object_actros.is_valid_for_route(route))

    def test_displayInfoCorrectOutput(self):
        # Arrange
        object_actros = Actros()

        # Act
        output = "\n".join(
            [
                f"ID: {object_actros.id}",
                f"Make: {'Actros'}",
                f"Weight Capacity: {26000}",
                f"Range: {13000}",
            ])

        # Assert
        self.assertEqual(object_actros.display_info(), output)
