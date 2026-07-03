from core.router import Router

class Orchestrator:

    def __init__(self):

        self.router = Router()

    def process(self, text):

        agent = self.router.route(text)

        print(f"[Router] -> {agent}")

        return agent