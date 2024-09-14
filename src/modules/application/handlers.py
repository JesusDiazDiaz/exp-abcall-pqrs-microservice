import logging
from src.modules.infrastructure.dispatchers import Dispatcher
from src.seedwork.application.handlers import Handler

LOGGER = logging.getLogger()


class CreateIncidentHandler(Handler):

    @staticmethod
    def handle_create_incident(event):
        LOGGER.info("handle create incident and send event to dispatcher")

        dispatcher = Dispatcher()
        dispatcher.publish_command(event)