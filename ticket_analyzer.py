import pandas as pd

from logger import logger


def analyze_tickets(df: pd.DataFrame) -> dict:
    logger.info("Analyzing tickets")

    analysis = {
        "total_tickets": len(df),
        "tickets_by_category": df["category"].value_counts().to_dict(),
        "average_resolution_time": round(df["resolution_hours"].mean(), 2),
        "high_priority_tickets": len(df[df["priority"] == "High"]),
    }

    logger.info("Ticket analysis complete")
    return analysis
