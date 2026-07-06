from agents.base_agent import BaseAgent


class VisionAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Vision Agent",
            description="Analyzes images and visual input.",
            priority=6
        )

    def can_handle(self, user_input: str) -> bool:
        text = user_input.lower()

        keywords = [
            "image",
            "photo",
            "picture",
            "vision",
            "camera",
            "scan"
        ]

        return any(keyword in text for keyword in keywords)

    def execute(self, user_input: str):
        return "Vision Agent is not implemented yet."