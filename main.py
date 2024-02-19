from __future__ import annotations
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)


engine.start()

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
AssignTruck 1
exit
"""
