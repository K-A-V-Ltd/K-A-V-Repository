from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)


engine.start()

"""
--------input example---------
createRoute Mar 11 12:30 Sydney Brisbane Adelaide Perth
createRoute  Apr 1 11:30 Brisbane Perth Sydney
createRoute Apr 1 17:23 Adelaide Brisbane Sydney
createRoute Nov 22 18:43 Perth Sydney Brisbane
searchRoute Brisbane Perth
exit
"""
