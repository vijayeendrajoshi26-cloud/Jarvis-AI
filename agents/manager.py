from agents.assistant_agent import AssistantAgent
from agents.memory_agent import MemoryAgent
from agents.automation_agent import AutomationAgent
from agents.browser_agent import BrowserAgent
from agents.file_agent import FileAgent
from agents.coding_agent import CodingAgent
from agents.vision_agent import VisionAgent
from agents.voice_agent import VoiceAgent
from agents.system_agent import SystemAgent
from agents.planning_agent import PlanningAgent
from agents.knowledge_agent import KnowledgeAgent
from agents.learning_agent import LearningAgent


class AgentManager:

    def __init__(self):

        self.agents = []

        self.register(MemoryAgent())
        self.register(AutomationAgent())
        self.register(BrowserAgent())
        self.register(FileAgent())
        self.register(CodingAgent())
        self.register(VisionAgent())
        self.register(VoiceAgent())
        self.register(SystemAgent())
        self.register(PlanningAgent())
        self.register(KnowledgeAgent())
        self.register(LearningAgent())
        self.register(AssistantAgent())  # Fallback agent

    def register(self, agent):
        self.agents.append(agent)

    def get_agent(self, user_input):

        for agent in self.agents:

            if agent.is_active() and agent.can_handle(user_input):
                return agent

        return None

    def list_agents(self):
        return [agent.info() for agent in self.agents]