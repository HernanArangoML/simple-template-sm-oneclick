"""settings state machine values"""
from typing import Dict, List
from app.prediction.state_machine_definition.states.end import End
from app.prediction.state_machine_definition.states.receive_answer import ReceiveAnswer
from app.prediction.state_machine_definition.states.receive_context import ReceiveContext
from app.prediction.state_machine_definition.states.receive_problem import ReceiveProblem
from app.prediction.state_machine_definition.states.request_context import RequestContext
from app.prediction.state_machine_definition.states.request_question import RequestQuestion
from ml_state_machine.factory.state import State


states: Dict[str, State] = {
    "receive_problem": ReceiveProblem("receive_answer"),
    "request_question": RequestQuestion("request_question"),
    "request_context": RequestContext("request_context"),
    "receive_answer": ReceiveAnswer("receive_answer"),
    "receive_context":  ReceiveContext("receive_context"),
    "end": End("end")
}

transitions: Dict[str, List[str]] = {
    "receive_problem": ["request_question", "request_context"],
    "request_question": ["receive_answer"],
    "request_context": ["receive_context"],
    "receive_answer": ["end", "request_context"],
    "receive_context": ["end"]
}
