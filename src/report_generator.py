from pathlib import Path

import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from .logger import logger

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)


def generate_excel_report(df: pd.DataFrame) -> Path:
    output_path = REPORTS_DIR / "ticket_report.xlsx"
    df.to_excel(output_path, index=False)
    logger.info("Excel report generated: %s", output_path)
    return output_path


def generate_pdf_summary(analysis: dict) -> Path:
    output_path = REPORTS_DIR / "ticket_summary.pdf"

    c = canvas.Canvas(str(output_path), pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "IT Ticket Automation Summary")

    c.setFont("Helvetica", 12)
    y = height - 100

    for key, value in analysis.items():
        c.drawString(50, y, f"{key.replace('_', ' ').title()}: {value}")
        y -= 25

    c.showPage()
    c.save()

    logger.info("PDF summary generated: %s", output_path)
    return output_path
