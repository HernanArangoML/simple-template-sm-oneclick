"""State End"""
from ml_state_machine.factory.state import State
from app.prediction.state_machine_definition.states.handlers.end_handler import EndHandler


class End(State):
    """Receive problem class"""

    def __init__(self):
        """constructor"""
        super(End, self).__init__()

    def handle(self, payload: dict) -> str:
        """handle a payload"""
        response = EndHandler.handle(payload)
        return response
