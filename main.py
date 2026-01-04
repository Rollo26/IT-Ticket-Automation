from logger import logger
from ticket_analyzer import analyze_tickets
from ticket_classifier import classify_ticket
from ticket_loader import load_tickets


def main():
    logger.info("IT Ticket Automation started")

    df = load_tickets("data/tickets.csv")

    df["category"] = df["description"].apply(classify_ticket)

    results = analyze_tickets(df)

    logger.info("Analysis Results:")
    for key, value in results.items():
        logger.info(f"{key}: {value}")

    logger.info("Automation finished successfully")


if __name__ == "__main__":
    main()
