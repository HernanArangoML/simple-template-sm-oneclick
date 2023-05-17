"""State Receive Context"""
from ml_state_machine.factory.state import State
from app.prediction.state_machine_definition.states.handlers.request_context_handler import RequestContextHandler


class RequestContext(State):
    """Receive problem class"""

    def __init__(self):
        """constructor"""
        super(RequestContext, self).__init__()

    def handle(self, payload: dict) -> str:
        """handle a payload"""

        response = RequestContextHandler.handle(payload)

        if response == "Receive Context":
            self.context.transition_to("receive_context")

        return response
