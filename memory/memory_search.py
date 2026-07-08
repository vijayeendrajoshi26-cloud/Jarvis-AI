import json
import os

from memory.short_term import ShortTermMemory
from memory.long_term import LongTermMemory


class MemorySearch:

    def __init__(self):

        self.short_memory = ShortTermMemory()
        self.long_memory = LongTermMemory()

        self.profile_file = "memory/profile.json"
        self.projects_file = "memory/projects.json"

    def search(self, keyword):

        keyword = keyword.lower()

        results = {
            "profile": {},
            "projects": {},
            "long_term": {},
            "short_term": {}
        }

        # ---------------- Profile ----------------

        if os.path.exists(self.profile_file):

            with open(self.profile_file, "r") as f:
                profile = json.load(f)

            for key, value in profile.items():

                if keyword in key.lower() or keyword in str(value).lower():
                    results["profile"][key] = value

        # ---------------- Projects ----------------

        if os.path.exists(self.projects_file):

            with open(self.projects_file, "r") as f:
                projects = json.load(f)

            for key, value in projects.items():

                if keyword in key.lower() or keyword in str(value).lower():
                    results["projects"][key] = value

        # ---------------- Long-Term ----------------

        memories = self.long_memory.list_memories()

        for key, value in memories.items():

            if keyword in key.lower() or keyword in str(value).lower():
                results["long_term"][key] = value

        # ---------------- Short-Term ----------------

        memories = self.short_memory.list_memories()

        for key, value in memories.items():

            if keyword in key.lower() or keyword in str(value).lower():
                results["short_term"][key] = value

        return results