import json
import os


class ProfileManager:

    def __init__(self):

        self.file = "memory/profile.json"

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump({}, f, indent=4)

    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, data):

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def remember(self, key, value):

        data = self.load()
        data[key] = value
        self.save(data)

    def recall(self, key):

        data = self.load()
        return data.get(key)

    def update(self, key, value):

        data = self.load()

        if key not in data:
            return False

        data[key] = value
        self.save(data)

        return True

    def forget(self, key):

        data = self.load()

        if key not in data:
            return False

        del data[key]

        self.save(data)

        return True

    def list_profile(self):

        return self.load()