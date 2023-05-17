"""State Receive Context"""
from ml_state_machine.factory.state import State
from app.prediction.state_machine_definition.states.handlers.receive_context_handler import ReceiveContextHandler


class ReceiveContext(State):
    """Receive context class"""

    def __init__(self):
        """constructor"""
        super(ReceiveContext, self).__init__()

    def handle(self, payload: dict) -> str:
        """handle a payload"""

        response = ReceiveContextHandler.handle(payload)

        if response == "End":
            self.context.transition_to("end")

        return response
