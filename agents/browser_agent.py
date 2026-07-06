from agents.base_agent import BaseAgent


class BrowserAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Browser Agent",
            description="Handles web browsing and internet searches.",
            priority=3
        )

    def can_handle(self, user_input: str) -> bool:

        text = user_input.lower()

        keywords = [
            "search",
            "google",
            "browser",
            "website",
            "internet",
            "web"
        ]

        return any(keyword in text for keyword in keywords)

    def execute(self, user_input: str):

        text = user_input.lower()

        if "search" in text:
            return "Browser Agent: Search functionality will be added soon."

        elif "open website" in text:
            return "Browser Agent: Website opening will be added soon."

        return "Browser Agent couldn't understand the request."