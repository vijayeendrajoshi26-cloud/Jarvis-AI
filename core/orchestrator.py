from agents.manager import AgentManager


class Orchestrator:

    def __init__(self):
        self.manager = AgentManager()

    def process(self, user_input):

        print("STEP 1")

        agent = self.manager.get_agent(user_input)

        if agent is None:
            return "Sorry, I don't know how to handle that."

        print("Selected Agent ->", agent.name)

        response = agent.execute(user_input)

        print("Response ->", response)

        return response