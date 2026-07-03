import os
from core.logger import get_logger

logger = get_logger()


def initialize():
    folders = [
        "data/logs",
        "data/cache",
        "data/temp",
        "memory",
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    logger.info("Startup completed.")