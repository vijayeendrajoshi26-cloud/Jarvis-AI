import json
import os
from datetime import datetime

from memory.profile_manager import ProfileManager
from memory.project_manager import ProjectManager


class MemoryManager:

    def __init__(self):

        self.file = "memory/memory.json"

        self.profile = ProfileManager()
        self.projects = ProjectManager()

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump({}, f, indent=4)

    # ==========================================================
    # File Handling
    # ==========================================================

    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, data):

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    # ==========================================================
    # Long-Term Memory
    # ==========================================================

    def remember(self, key, value, category="general", importance=3):

        data = self.load()

        data[key] = {
            "value": value,
            "category": category,
            "importance": importance,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "last_accessed": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.save(data)

    def recall(self, key):

        data = self.load()

        if key in data:

            data[key]["last_accessed"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.save(data)

            return data[key]["value"]

        return None

    def update(self, key, new_value):

        data = self.load()

        if key in data:

            data[key]["value"] = new_value

            data[key]["last_accessed"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.save(data)

            return True

        return False

    def forget(self, key):

        data = self.load()

        if key in data:

            del data[key]

            self.save(data)

            return True

        return False

    def list_memories(self):

        return self.load()

    def search(self, keyword):

        data = self.load()

        keyword = keyword.lower()

        results = {}

        for key, value in data.items():

            if keyword in key.lower() or keyword in value["value"].lower():

                results[key] = value

        return results

    # ==========================================================
    # Profile Memory
    # ==========================================================

    def remember_profile(self, key, value):

        self.profile.remember(key, value)

    def recall_profile(self, key):

        return self.profile.recall(key)

    def update_profile(self, key, value):

        return self.profile.update(key, value)

    def forget_profile(self, key):

        return self.profile.forget(key)

    def list_profile(self):

        return self.profile.list_profile()

    # ==========================================================
    # Project Memory
    # ==========================================================

    def create_project(self, project_name):

        return self.projects.create_project(project_name)

    def get_project(self, project_name):

        return self.projects.get_project(project_name)

    def update_project_module(self, project_name, module):

        return self.projects.update_module(project_name, module)

    def complete_project_module(self, project_name, module):

        return self.projects.complete_module(project_name, module)

    def list_projects(self):

        return self.projects.list_projects()
        
    def set_active_project(self, project_name):
        
        return self.projects.set_active_project(project_name)

    def get_active_project(self):
        
        return self.projects.get_active_project()

    def clear_active_project(self):
        
        return self.projects.clear_active_project()

    # ==========================================================
    # Unified Recall
    # ==========================================================

    def recall_any(self, key):

        key = key.lower()

        # Profile
        profile = self.recall_profile(key)

        if profile:
            return profile, "Profile Memory"

        # Project
        projects = self.list_projects()

        for project_name, project_data in projects.items():

            if project_name.lower() == key:

                return project_data, "Project Memory"

        # Long-Term
        memory = self.recall(key)

        if memory:
            return memory, "Long-Term Memory"

        return None, None