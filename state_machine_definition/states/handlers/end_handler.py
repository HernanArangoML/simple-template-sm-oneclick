"""End Handler"""


class EndHandler:
    """ReceiveProblemHandler class"""

    @staticmethod
    def handle(payload: dict) -> str:
        """
        handle a payload
        Args:
            - payload: Payload
        Returns:
            - str
        """

        return "End"
