from agents.base_agent import BaseAgent


class LearningAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Learning Agent",
            description="Learns user preferences and improves over time.",
            priority=9
        )

    def can_handle(self, user_input: str) -> bool:

        text = user_input.lower()

        keywords = [
            "learn",
            "improve",
            "habit",
            "preference",
            "remember this pattern"
        ]

        return any(keyword in text for keyword in keywords)

    def execute(self, user_input: str):

        return "Learning Agent: Learning system will be added soon."