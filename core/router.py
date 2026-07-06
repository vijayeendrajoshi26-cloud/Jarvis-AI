def route(text):
    text = text.lower()

    if "remember" in text:
        return "memory"

    if "what is my" in text:
        return "memory"

    return "assistant"