"""Payload"""


class Payload:
    """Payload class as a DTO"""

    def __init__(self, user_text: str) -> None:
        self.user_text = user_text
