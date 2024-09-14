import logging
from dataclasses import dataclass
from pydispatch import dispatcher
from src.modules.application.commands.base import CommandBaseHandler
from src.seedwork.application.commands import execute_command
from src.seedwork.application.commands import Command

LOGGER = logging.getLogger()


@dataclass
class CreateIncidentCommand(Command):
    incidence_type: str
    status: str
    risk_level: str


class UpdateInformationHandler(CommandBaseHandler):
    def handle(self, command: CreateIncidentCommand):
        LOGGER.info("Handle createIncidentCommand")

        dispatcher.send(signal='CreateIncidentIntegration', event=command)


@execute_command.register(CreateIncidentCommand)
def execute_update_information_command(command:  CreateIncidentCommand):
    handler = UpdateInformationHandler()
    handler.handle(command)
