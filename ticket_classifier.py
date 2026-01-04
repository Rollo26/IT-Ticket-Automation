from .logger import logger

NETWORK_KEYWORDS = ["wifi", "network", "internet"]
ACCESS_KEYWORDS = ["password", "login", "access"]
SOFTWARE_KEYWORDS = ["outlook", "email", "software"]
HARDWARE_KEYWORDS = ["printer", "hardware", "keyboard"]


def classify_ticket(description: str) -> str:
    description = description.lower()

    if any(word in description for word in NETWORK_KEYWORDS):
        category = "Network"
    elif any(word in description for word in ACCESS_KEYWORDS):
        category = "Access"
    elif any(word in description for word in SOFTWARE_KEYWORDS):
        category = "Software"
    elif any(word in description for word in HARDWARE_KEYWORDS):
        category = "Hardware"
    else:
        category = "Other"

    logger.debug("Ticket classified as %s", category)
    return category
