class Router:

    def route(self, text: str):

        text = text.lower()

        if "remember" in text:
            return "memory"

        elif "open" in text:
            return "automation"

        else:
            return "assistant"