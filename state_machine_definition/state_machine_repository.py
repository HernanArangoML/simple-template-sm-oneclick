# pylint: disable=redefined-builtin
"""StateMachineRepository"""
from typing import Optional
from ml_state_machine.repositories.concrete_repository import ConcreteRepository
from ml_state_machine.factory.state import State
from app.lib.db_engines.cache import Cache
from app.settings import KVS_STATES
from app.settings import TTL_STATES
from app.prediction.state_machine_definition.settings import states


class StateMachineRepository(ConcreteRepository):
    """State Machine Repository class"""

    def __init__(self) -> None:
        super().__init__()
        self.cache = Cache(KVS_STATES)

    def get(self, identifier: str) -> Optional[State]:
        """
        Returns a state by an id
        Args:
            - identifier: str
        Returns:
            - State or None
        """
        result = self.cache.get(identifier)
        if result:
            return states[result["state_name"]]
        return None

    def save(self, identifier: str, state: State) -> None:
        """
        Save a tuple (identifier, state) in a repository
        Args:
            - id: str
        Returns:
            -  None
        """
        data = {"state_name": state.name}
        self.cache.save(identifier, data, TTL_STATES)
