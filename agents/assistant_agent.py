from agents.base_agent import BaseAgent


class AssistantAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Assistant Agent",
            description="Handles greetings and general conversation.",
            priority=100
        )

    def can_handle(self, user_input: str) -> bool:
        """
        AssistantAgent is the fallback agent.
        It always returns True, so it should be registered LAST.
        """
        return True

    def execute(self, user_input: str):

        text = user_input.lower()

        greetings = [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ]

        if any(greet in text for greet in greetings):
             return "Hello! I'm Jarvis. How can I help you today."

        elif text == "how are you":
            return "I'm doing great and ready to help."

        elif text == "who are you":
            return "I'm Jarvis, your personal AI assistant."

        else:
            return f"I understood your request: {user_input}"