from agents.base_agent import BaseAgent


class KnowledgeAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Knowledge Agent",
            description="Answers factual questions and provides information.",
            priority=8
        )

    def can_handle(self, user_input: str) -> bool:

        text = user_input.lower()

        keywords = [
            "who",
            "when",
            "where",
            "why",
            "how",
            "tell me",
            "information"
        ]

        return any(keyword in text for keyword in keywords)

    def execute(self, user_input: str):

        return "Knowledge Agent: Knowledge retrieval will be added soon."