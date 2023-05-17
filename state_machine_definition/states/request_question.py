"""State Request Question"""
from ml_state_machine.factory.state import State
from app.prediction.state_machine_definition.states.handlers.request_question_handler import RequestQuestionHandler


class RequestQuestion(State):
    """Receive problem class"""

    def __init__(self):
        """constructor"""
        super(RequestQuestion, self).__init__()

    def handle(self, payload: dict) -> str:
        """handle a payload"""

        response = RequestQuestionHandler.handle(payload)
        if response == "Receive Answer":
            self.context.transition_to("receive_answer")

        return response
