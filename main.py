from __future__ import annotations
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)


engine.start()

"""
TO-DOs:
- expand and add more unit tests 
- fix the unit tests which are not working properly 
- handle the truck's movement from one route to another in a more logical way, instead of accounting just the lack of overlap in the start and end time
-check comments in different modules 
-add detailed docstrings
"""


"""
-------- input examples ---------

viewunassignedPackages
viewPackageInfo 2
registerPackage Sydney Brisbane 23.5 John Dutton 0386574856 john.dutton@gmail.com
registerPackage Perth Adelaide 53.5 John Dutton 0386574856 john.dutton@gmail.com
viewunassignedPackages
viewPackageInfo 2
createRoute Mar 11 12:30 Sydney Brisbane Adelaide Perth
createRoute  Apr 1 11:30 Brisbane Perth Sydney
createRoute Apr 1 17:23 Perth Brisbane Adelaide Sydney
AssignTruck 3
createRoute Nov 22 18:43 Perth Sydney Brisbane
searchRoute Perth Adelaide
assignPackage 2 3
viewPackageInfo 2

-----for bulk assign------
registerPackage Sydney Brisbane 20.5 Jane Smith 0498237456 jane.smith@gmail.com
registerPackage Sydney Brisbane 22.0 Michael Johnson 0412345678 michael.johnson@gmail.com
registerPackage Sydney Brisbane 21.8 Emily Brown 0432156897 emily.brown@gmail.com
registerPackage Sydney Brisbane 23.2 David Wilson 0478963214 david.wilson@gmail.com
registerPackage Sydney Brisbane 24.0 Olivia Jones 0456789231 olivia.jones@gmail.com
registerPackage Sydney Brisbane 19.7 James Taylor 0489753102 james.taylor@gmail.com
registerPackage Sydney Brisbane 22.5 Sophia Martinez 0423568970 sophia.martinez@gmail.com
registerPackage Sydney Brisbane 21.0 Benjamin Anderson 0498765432 benjamin.anderson@gmail.com
registerPackage Sydney Brisbane 23.8 Mia Thomas 0467890123 mia.thomas@gmail.com
registerPackage Sydney Brisbane 20.0 Ethan Jackson 0432109876 ethan.jackson@gmail.com





registerPackage Adelaide Brisbane 13.4 Ethan Jackson 0432109876 ethan.jackson@gmail.com
registerPackage AliceSprings Perth 29.2 Mia Thomas 0467890123 mia.thomas@gmail.com
registerPackage Brisbane Darwin 13.5 Sophia Martinez 0423568970 sophia.martinez@gmail.com
exit
"""
