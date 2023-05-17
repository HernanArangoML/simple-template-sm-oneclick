"""State Receive Answer"""
from ml_state_machine.factory.state import State
from app.prediction.state_machine_definition.states.handlers.receive_answer_handler import ReceiveAnswerHandler


class ReceiveAnswer(State):
    """Receive answer class"""

    def __init__(self):
        """constructor"""
        super(ReceiveAnswer, self).__init__()

    def handle(self, payload: dict) -> str:
        """handle a payload"""

        response = ReceiveAnswerHandler.handle(payload)

        if response == "End":
            self.context.transition_to("end")

        if response == "Request Context":
            self.context.transition_to("requested_context")

        return response
