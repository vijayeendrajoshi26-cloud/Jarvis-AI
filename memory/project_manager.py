import json
import os


class ProjectManager:

    def __init__(self):

        self.file = "memory/projects.json"
        self.active_project_file = "memory/active_project.json"

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump({}, f, indent=4)

        if not os.path.exists(self.active_project_file):
            with open(self.active_project_file, "w") as f:
                json.dump({"active_project": None}, f, indent=4)

    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, data):

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def create_project(self, name):

        data = self.load()

        if name in data:
            return False

        data[name] = {
            "status": "Active",
            "current_module": "",
            "completed_modules": [],
            "progress": 0
        }

        self.save(data)
        self.set_active_project(name)

        return True

    def update_module(self, name, module):

        data = self.load()

        if name not in data:
            return False

        data[name]["current_module"] = module

        self.save(data)

        return True

    def complete_module(self, name, module):

        data = self.load()

        if name not in data:
            return False

        if module not in data[name]["completed_modules"]:
            data[name]["completed_modules"].append(module)

        total_modules = 10
        completed = len(data[name]["completed_modules"])

        data[name]["progress"] = int((completed / total_modules) * 100)

        self.save(data)

        return True

    def get_project(self, name):

        data = self.load()

        return data.get(name)

    def list_projects(self):

        return self.load()

    def delete_project(self, name):

        data = self.load()

        if name not in data:
            return False

        del data[name]

        self.save(data)

        return True

    # --------------------------------------------------
    # Active Project
    # --------------------------------------------------

    def set_active_project(self, name):

        data = self.load()

        if name not in data:
            return False

        with open(self.active_project_file, "w") as f:
            json.dump({"active_project": name}, f, indent=4)

        return True

    def get_active_project(self):

        with open(self.active_project_file, "r") as f:
            data = json.load(f)

        return data.get("active_project")

    def clear_active_project(self):

        with open(self.active_project_file, "w") as f:
            json.dump({"active_project": None}, f, indent=4)

        return True