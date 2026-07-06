from agents.base_agent import BaseAgent


class FileAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="File Agent",
            description="Manages files and folders.",
            priority=4
        )

    def can_handle(self, user_input: str) -> bool:

        text = user_input.lower()

        keywords = [
            "file",
            "folder",
            "document",
            "pdf",
            "excel",
            "word"
        ]

        return any(keyword in text for keyword in keywords)

    def execute(self, user_input: str):

        text = user_input.lower()

        if "pdf" in text:
            return "File Agent: PDF reader will be added soon."

        elif "word" in text:
            return "File Agent: Word document support will be added soon."

        elif "excel" in text:
            return "File Agent: Excel support will be added soon."

        elif "file" in text:
            return "File Agent: File management will be added soon."

        elif "folder" in text:
            return "File Agent: Folder management will be added soon."

        return "File Agent couldn't understand the request."