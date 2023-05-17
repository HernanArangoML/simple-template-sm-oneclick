from ml_state_machine.setup import state_machine_factory
from ml_state_machine.factory.context import Context
from state_machine_definition.settings import states, transitions
from state_machine_definition.state_machine_repository import StateMachineRepository
from state_machine_definition.states.handlers.entities.payload import Payload

# Initialize the factory
state_machine_factory.initialize(
    app_name="oneclick",
    init_state_name="received_problem",
    states=states,
    transitions=transitions,
    repository=StateMachineRepository(),
    run_local=True,
)
chat_id = "123456987"
conversation: Context = state_machine_factory.get_context(chat_id)

payload = Payload(user_text="bom dia")

# Handle the payload. Execute business logic of current state
response = conversation.handle(payload.__dict__)
