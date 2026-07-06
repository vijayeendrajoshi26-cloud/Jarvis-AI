from agents.base_agent import BaseAgent


class PlanningAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Planning Agent",
            description="Plans tasks, schedules, and goals.",
            priority=7
        )

    def can_handle(self, user_input: str) -> bool:

        text = user_input.lower()

        keywords = [
            "plan",
            "planning",
            "goal",
            "goals",
            "daily plan",
            "weekly plan"
        ]

        return any(keyword in text for keyword in keywords)

    def execute(self, user_input: str):

        return "Planning Agent: Planning feature will be added soon."