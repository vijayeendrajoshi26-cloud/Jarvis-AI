from agents.base_agent import BaseAgent


class SystemAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="System Agent",
            description="Monitors and controls the computer system.",
            priority=10
        )

    def can_handle(self, user_input: str) -> bool:

        text = user_input.lower()

        keywords = [
            "battery",
            "cpu",
            "ram",
            "storage",
            "system",
            "wifi",
            "bluetooth"
        ]

        return any(keyword in text for keyword in keywords)

    def execute(self, user_input: str):

        return "System Agent: System monitoring will be added soon."