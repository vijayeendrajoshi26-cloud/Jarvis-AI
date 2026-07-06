from agents.base_agent import BaseAgent


class VoiceAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Voice Agent",
            description="Handles speech recognition and voice interaction.",
            priority=6
        )

    def can_handle(self, user_input: str) -> bool:

        text = user_input.lower()

        keywords = [
            "voice",
            "speech",
            "microphone",
            "listen",
            "speak",
            "enable voice",
            "disable voice"
        ]

        return any(keyword in text for keyword in keywords)

    def execute(self, user_input: str):

        text = user_input.lower()

        if "enable voice" in text:
            return "Voice Agent: Voice mode will be added soon."

        elif "disable voice" in text:
            return "Voice Agent: Voice mode will be disabled soon."

        elif "speech" in text:
            return "Voice Agent: Speech recognition will be added soon."

        elif "microphone" in text:
            return "Voice Agent: Microphone support will be added soon."

        return "Voice Agent: Voice features will be added soon."