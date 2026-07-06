from agents.base_agent import BaseAgent
from memory.memory_manager import MemoryManager


class MemoryAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Memory Agent",
            description="Stores and recalls user information.",
            priority=1
        )

        self.memory = MemoryManager()

    def can_handle(self, user_input: str) -> bool:

        text = user_input.lower().strip()

        return (
            text.startswith("remember") or
            text.startswith("what is my") or
            text.startswith("forget") or
            text.startswith("update") or
            text.startswith("what do you know about me")
        )

    def execute(self, user_input: str):

        text = user_input.lower().strip()

        # ---------- Remember ----------
        if text.startswith("remember"):

            content = user_input[9:].strip()

            if " is " in content:

                key, value = content.split(" is ", 1)

                key = key.strip().lower()

                if key.startswith("my "):
                    key = key[3:]

                self.memory.remember(key, value.strip())

                return f"I'll remember that your {key} is {value.strip()}."

            return "Please say: Remember my favorite color is blue."

        # ---------- Recall ----------
        elif text.startswith("what is my"):

            key = user_input[11:].strip().lower()

            value = self.memory.recall(key)

            if value:
                return f"Your {key} is {value}."

            return "I don't know that yet."

        return "Memory Agent couldn't understand the request."