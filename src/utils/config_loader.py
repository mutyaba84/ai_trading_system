import yaml
from src.utils.logger import get_logger

logger = get_logger("ConfigLoader")

def load_config(path="configs/config.yaml"):
    try:
        with open(path, 'r') as f:
            config = yaml.safe_load(f)
        logger.info(f"Configuration loaded from {path}")
        return config
    except Exception as e:
        logger.error(f"Failed to load config: {e}")
        return {}
