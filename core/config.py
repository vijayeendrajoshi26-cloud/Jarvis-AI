"""
Global configuration for Jarvis.
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_NAME = os.getenv("ASSISTANT_NAME", "Jarvis")
    USER_NAME = os.getenv("USER_NAME", "User")
    MODEL = os.getenv("MODEL", "gpt-4.1")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

config = Config()