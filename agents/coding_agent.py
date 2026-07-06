from agents.base_agent import BaseAgent


class CodingAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Coding Agent",
            description="Helps with programming, debugging, and code generation.",
            priority=5
        )

    def can_handle(self, user_input: str) -> bool:

        text = user_input.lower()

        keywords = [
            "code",
            "python",
            "java",
            "c++",
            "bug",
            "debug",
            "program",
            "script",
            "function",
            "review"
        ]

        return any(keyword in text for keyword in keywords)

    def execute(self, user_input: str):

        text = user_input.lower()

        if "python" in text:
            return "Coding Agent: Python code generation will be added soon."

        elif "debug" in text:
            return "Coding Agent: Debugger will be added soon."

        elif "review" in text:
            return "Coding Agent: Code review will be added soon."

        elif "function" in text:
            return "Coding Agent: Function generation will be added soon."

        return "Coding Agent: Coding features will be added soon."