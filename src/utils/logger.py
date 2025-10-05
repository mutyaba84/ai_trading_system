# /app/src/utils/logger.py

import logging
import sys


def get_logger(name: str):
    """
    Creates and returns a logger with a standard format.
    Logs both to console and can be extended for file logging.
    """
    logger = logging.getLogger(name)

    # Avoid duplicate handlers if logger already exists
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger
