"""State Receive Problem"""
from ml_state_machine.factory.state import State
from app.prediction.state_machine_definition.states.handlers.receive_problem_handler import ReceiveProblemHandler


class ReceiveProblem(State):
    """Receive problem class"""

    def __init__(self):
        """constructor"""
        super(ReceiveProblem, self).__init__()

    def handle(self, payload: dict) -> str:
        """handle a payload"""

        response = ReceiveProblemHandler.handle(payload)

        if response == "Request Question":
            self.context.transition_to("requested_question")

        if response == "Request Context":
            self.context.transition_to("requested_context")

        if response == "End":
            self.context.transition_to("requested_context")

        return response
