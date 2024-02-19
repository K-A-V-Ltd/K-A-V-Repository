import unittest
from commands.view_routes import ViewActiveRoutesCommand
from core.application_data import ApplicationData
from models.location import Location
from models.vehicles.trucks_creation import Garage
import utils.time_abstraction as abstraction
from datetime import datetime
from models.route import Route


class ViewRoutesCommandShould(unittest.TestCase):
    def test_executePrintsAppropriateInformation_forEachRouteDependingOnRouteStatus_andTime(self):
        abstraction.my_current_time = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        APP_DATA = ApplicationData()
        loc1 = Location("Brisbane")
        loc2 = Location("Perth")
        loc3 = Location("Sydney")
        loc4 = Location("Adelaide")
        loc5 = Location("Darwin")
        start1 = datetime.strptime("Feb 18 12:00", "%b %d %H:%M")
        start2 = datetime.strptime("Feb 20 12:00", "%b %d %H:%M")
        start3 = datetime.strptime("Feb 24 12:00", "%b %d %H:%M")
        start4 = datetime.strptime("Feb 28 12:00", "%b %d %H:%M")
        start5 = datetime.strptime("Mar 8 12:00", "%b %d %H:%M")
        tst_route1 = Route(1, start1, [loc1, loc2, loc3])
        tst_route2 = Route(2, start2, [loc2, loc3, loc4])
        tst_route3 = Route(3, start3, [loc3, loc4, loc5])
        tst_route4 = Route(4, start4, [loc1, loc2, loc3, loc4, loc5])
        tst_route5 = Route(5, start5, [loc2, loc4, loc5, loc3, loc1])
        truck1, truck2, truck3, truck4, truck5 = Garage[:5]
        tst_route1.truck, tst_route2.truck, tst_route3.truck, tst_route4.truck, tst_route5.truck = truck1, truck2, truck3, truck4, truck5
        APP_DATA.add_route(tst_route1)
        APP_DATA.add_route(tst_route2)
        APP_DATA.add_route(tst_route3)
        APP_DATA.add_route(tst_route4)
        APP_DATA.add_route(tst_route5)
        expected = "Route ID: 1\n" \
                   "Brisbane (Mar 13 14:28) -> Perth (Mar 08 12:00) -> Sydney (Mar 13 04:02)\n" \
                   "Delivery Weight: 0\n" \
                   "Next Stop: Perth\n" \
                   "\n" \
                   "Route ID: 2\n" \
                   "Perth (Mar 08 12:00) -> Sydney (Mar 13 04:02) -> Adelaide (Mar 09 20:00)\n" \
                   "Delivery Weight: 0\n" \
                   "Next Stop: Perth\n" \
                   "\n" \
                   "Route ID: 3\n" \
                   "Sydney (Mar 13 04:02) -> Adelaide (Mar 09 20:00) -> Darwin (Mar 11 06:48)\n" \
                   "Delivery Weight: 0\n" \
                   "Next Stop: Adelaide\n" \
                   "\n"
        tst_command = ViewActiveRoutesCommand([], APP_DATA)
        self.assertEqual(expected, tst_command.execute())
