from abc import ABC, abstractmethod
from datetime import datetime


class BaseAgent(ABC):
    """
    Base class for every JARVIS agent.
    """

    def __init__(self, name: str, description: str, priority: int = 5):
        self.name = name
        self.description = description
        self.priority = priority
        self.active = True
        self.created_at = datetime.now()

    @abstractmethod
    def can_handle(self, user_input: str) -> bool:
        """
        Return True if this agent can handle the request.
        """
        pass

    @abstractmethod
    def execute(self, user_input: str):
        """
        Execute the task and return a response.
        """
        pass

    def start(self):
        self.active = True

    def stop(self):
        self.active = False

    def is_active(self):
        return self.active

    def health(self):
        return {
            "name": self.name,
            "status": "Active" if self.active else "Inactive",
            "priority": self.priority,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def info(self):
        return {
            "name": self.name,
            "description": self.description,
            "priority": self.priority
        }

    def __str__(self):
        return f"{self.name} ({'Active' if self.active else 'Inactive'})"