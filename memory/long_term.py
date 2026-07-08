from memory.memory_manager import MemoryManager


class LongTermMemory:

    def __init__(self):
        self.memory = MemoryManager()

    def remember(self, key, value, category="general", importance=3):
        self.memory.remember(key, value, category, importance)

    def recall(self, key):
        return self.memory.recall(key)

    def update(self, key, value):
        return self.memory.update(key, value)

    def forget(self, key):
        return self.memory.forget(key)

    def list_memories(self):
        return self.memory.list_memories()

    def search(self, keyword):
        return self.memory.search(keyword)
