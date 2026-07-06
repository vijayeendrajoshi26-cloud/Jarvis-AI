from agents.base_agent import BaseAgent
import os


class AutomationAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Automation Agent",
            description="Controls applications and performs automation tasks.",
            priority=2
        )

    def can_handle(self, user_input: str) -> bool:

        text = user_input.lower()

        keywords = [
            "reminder",
            "remind",
            "alarm",
            "timer",
            "schedule",
            "automation",
            "task",
            "open notepad",
            "open calculator",
            "open paint",
            "open explorer",
            "open file explorer"
        ]

        return any(keyword in text for keyword in keywords)

    def execute(self, user_input: str):

        text = user_input.lower()

        if "open notepad" in text:
            os.system("start notepad")
            return "Opening Notepad."

        elif "open calculator" in text:
            os.system("start calc")
            return "Opening Calculator."

        elif "open paint" in text:
            os.system("start mspaint")
            return "Opening Paint."

        elif "open explorer" in text or "open file explorer" in text:
            os.system("start explorer")
            return "Opening File Explorer."

        elif "reminder" in text or "remind" in text:
            return "Automation Agent: Reminder feature will be added soon."

        return "Automation task not supported yet."