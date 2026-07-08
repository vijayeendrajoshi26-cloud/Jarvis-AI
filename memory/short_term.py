from datetime import datetime


class ShortTermMemory:

    def __init__(self):
        self.memories = {}

    def remember(self, key, value):

        self.memories[key] = {
            "value": value,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def recall(self, key):

        if key in self.memories:
            return self.memories[key]["value"]

        return None

    def forget(self, key):

        if key in self.memories:
            del self.memories[key]
            return True

        return False

    def clear(self):
        self.memories.clear()

    def list_memories(self):
        return self.memories
        