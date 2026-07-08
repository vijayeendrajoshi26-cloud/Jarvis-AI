from agents.base_agent import BaseAgent
from memory.short_term import ShortTermMemory
from memory.long_term import LongTermMemory
from memory.memory_search import MemorySearch
from memory.memory_manager import MemoryManager


class MemoryAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Memory Agent",
            description="Stores and manages user memories.",
            priority=1
        )

        self.short_memory = ShortTermMemory()
        self.long_memory = LongTermMemory()

        # Central memory manager
        self.memory = MemoryManager()

        self.search_engine = MemorySearch()

        # Waiting for user to choose short/long memory
        self.pending_memory = None

    def can_handle(self, user_input: str) -> bool:

        text = user_input.lower()

        if self.pending_memory:
            return True

        keywords = [
            "remember",
            "what is my",
            "forget",
            "update",
            "show all memories",
            "what do you know about me",
            "search",
            "module completed",
            "current module",
            "completed",
            "set active project",
            "show active project",
            "active project",
            "switch project"
        ]

        return any(keyword in text for keyword in keywords)

    def execute(self, user_input: str):

        # ==========================================================
        # Pending Memory Choice
        # ==========================================================

        if self.pending_memory:

            choice = user_input.lower().strip()

            key = self.pending_memory["key"]
            value = self.pending_memory["value"]

            if choice in ["short", "short-term", "temporary"]:

                self.short_memory.remember(key, value)

                self.pending_memory = None

                return f"Done! I'll remember your {key} for this session."

            elif choice in ["long", "long-term", "permanent"]:

                profile_keys = [
                    "name",
                    "age",
                    "city",
                    "profession",
                    "favorite color",
                    "favorite language",
                    "skill",
                    "skills"
                ]

                if key in profile_keys:

                    self.memory.remember_profile(key, value)

                elif key == "project":

                    self.memory.create_project(value)
                    self.memory.set_active_project(value)
                    self.long_memory.remember("project", value)

                else:

                    self.long_memory.remember(key, value)

                self.pending_memory = None

                return f"Done! I'll remember your {key} permanently."

            else:

                return "Please reply with 'short' or 'long'."

        text = user_input.lower()

        # ==========================================================
        # Remember
        # ==========================================================

        if text.startswith("remember"):

            content = user_input[9:].strip()

            if " is " in content:

                key, value = content.split(" is ", 1)

                key = key.strip().lower()

                if key.startswith("my "):
                    key = key[3:]

                self.pending_memory = {
                    "key": key,
                    "value": value.strip()
                }

                return (
                    f"Should I remember your {key} in:\n\n"
                    "• Short-Term Memory\n"
                    "• Long-Term Memory\n\n"
                    "Reply with: short or long"
                )

            return "Please say: Remember my favorite color is blue."

        # ==========================================================
        # Recall
        # ==========================================================

        elif text.startswith("what is my"):
            key = user_input[11:].strip()

            # Short-Term
            value = self.short_memory.recall(key.lower())

            if value:
                return f"Your {key} is {value}. (Short-Term Memory)"

            # Profile / Project / Long-Term
            value, source = self.memory.recall_any(key)
            if value:
                # If asking about project
                if key.lower() == "project":
                    project = self.memory.get_project(value)
                    if project:
                        return (
                            f"Project: {value}\n"
                            f"Status: {project['status']}\n"
                            f"Current Module: {project['current_module']}\n"
                            f"Completed Modules: {len(project['completed_modules'])}\n"
                            f"Progress: {project['progress']}%"
                        )

                return f"Your {key} is {value}. ({source})"
            return "I don't know that yet."
        # ==========================================================
        # Update
        # ==========================================================

        elif text.startswith("update"):

            content = user_input[6:].strip()

            if " to " in content:

                key, value = content.split(" to ", 1)

                key = key.strip().lower()

                if key.startswith("my "):
                    key = key[3:]

                if self.long_memory.update(key, value.strip()):
                    return f"Updated your {key}."

                return "I couldn't find that memory."

        # ==========================================================
        # Forget
        # ==========================================================

        elif text.startswith("forget"):

            key = user_input[6:].strip().lower()

            if key.startswith("my "):
                key = key[3:]

            if self.short_memory.forget(key):
                return f"I forgot your {key} from Short-Term Memory."

            if self.long_memory.forget(key):
                return f"I forgot your {key} from Long-Term Memory."

            return "I couldn't find that memory."

        # ==========================================================
        # Show All
        # ==========================================================

        elif text == "show all memories" or text == "what do you know about me":

            memories = self.long_memory.list_memories()

            if not memories:
                return "I don't know anything about you yet."

            output = []

            for key, value in memories.items():
                output.append(f"{key}: {value['value']}")

            return "\n".join(output)

        # ==========================================================
        # Search
        # ==========================================================

        elif text.startswith("search"):

            keyword = user_input[6:].strip()

            results = self.search_engine.search(keyword)

            output = []

            if results["profile"]:
                output.append("===== PROFILE =====")
                for key, value in results["profile"].items():
                    output.append(f"{key}: {value}")

            if results["projects"]:
                output.append("\n===== PROJECTS =====")
                for key, value in results["projects"].items():
                    output.append(f"{key}: {value}")

            if results["long_term"]:
                output.append("\n===== LONG TERM =====")
                for key, value in results["long_term"].items():
                    output.append(f"{key}: {value['value']}")

            if results["short_term"]:
                output.append("\n===== SHORT TERM =====")
                for key, value in results["short_term"].items():
                    output.append(f"{key}: {value['value']}")

            if not output:
                return "No matching memories found."

            return "\n".join(output)
        # ==========================================================
        # Project Progress
        # ==========================================================

        elif "module completed" in text:
            module = text.replace("module completed", "").strip().title()
            project_name = self.memory.get_active_project()
            if not project_name:
                return "No active project found."

            self.memory.complete_project_module(project_name, module)

            return f"{module} module marked as completed."

        elif text.startswith("current module"):
            module = user_input[14:].strip().title()

            project_name = self.memory.get_active_project()
            if not project_name:
                return "No active project found."

            self.memory.update_project_module(project_name, module)

            return f"Current module updated to {module}." 

        # ==========================================================
        # Active Project
        # ==========================================================

        elif text.startswith("set active project"):
            
            project = user_input[18:].strip()

            if self.memory.set_active_project(project):
                return f"{project} is now the active project."

            return "Project not found."

        elif text == "show active project":
            
            project_name = self.memory.get_active_project()

            if not project_name:
                return "No active project."

            project = self.memory.get_project(project_name)

            return (
                f"Active Project: {project_name}\n"
                f"Status: {project['status']}\n"
                f"Current Module: {project['current_module']}\n"
                f"Completed Modules: {len(project['completed_modules'])}\n"
                f"Progress: {project['progress']}%"
            )

        return "Memory Agent couldn't understand the request."