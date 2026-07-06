from core.startup import initialize
from core.orchestrator import Orchestrator
from core.config import config
import os

print("Running from:", os.getcwd())


def main():

    initialize()

    print("=" * 50)
    print(f" Welcome {config.USER_NAME}")
    print(f" {config.APP_NAME} Initializing...")
    print("=" * 50)

    orchestrator = Orchestrator()

    while True:

        user = input("\nYou : ")

        if user.lower() == "exit":
            break

        orchestrator.process(user)


if __name__ == "__main__":
    main()