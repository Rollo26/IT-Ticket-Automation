import pandas as pd
from src.logger import logger


def load_tickets(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Loaded {len(df)} tickets from {file_path}")
        return df
    except Exception as e:
        logger.error(f"Failed to load tickets: {e}")
        raise
