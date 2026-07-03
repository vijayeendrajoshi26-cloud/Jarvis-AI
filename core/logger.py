from loguru import logger
import os

LOG_FOLDER = "data/logs"

os.makedirs(LOG_FOLDER, exist_ok=True)

logger.add(
    f"{LOG_FOLDER}/jarvis.log",
    rotation="5 MB",
    level="INFO",
    format="{time} | {level} | {message}"
)

def get_logger():
    return logger