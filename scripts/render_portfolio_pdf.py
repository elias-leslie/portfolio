#!/usr/bin/env python3
"""Render portfolio Markdown sources to simple PDFs.

Run from the repository root:
  uv run --with reportlab python scripts/render_portfolio_pdf.py
"""
from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
JOBS = [
    (DOCS / "Detailed_Portfolio.md", DOCS / "Detailed_Portfolio.pdf"),
    (
        DOCS / "Elias_Leslie_Portfolio_Summary_Security_Automation.md",
        DOCS / "Elias_Leslie_Portfolio_Summary_Security_Automation.pdf",
    ),
]


def inline_markup(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`(.+?)`", r"<font name='Courier'>\1</font>", text)
    text = re.sub(r"&lt;(https?://[^&]+)&gt;", r"<link href='\1'>\1</link>", text)
    return text


def render(source: Path, output: Path) -> None:
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "PortfolioTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=27,
        textColor=colors.HexColor("#0f172a"),
        spaceAfter=14,
    )
    h2 = ParagraphStyle(
        "PortfolioH2",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#1e3a8a"),
        spaceBefore=12,
        spaceAfter=6,
    )
    body = ParagraphStyle(
        "PortfolioBody",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#1f2937"),
        spaceAfter=6,
    )
    bullet = ParagraphStyle(
        "PortfolioBullet",
        parent=body,
        leftIndent=16,
        bulletIndent=6,
    )
    story = []
    for raw in source.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            story.append(Spacer(1, 4))
        elif line.startswith("# "):
            story.append(Paragraph(inline_markup(line[2:]), title))
        elif line.startswith("## "):
            story.append(Paragraph(inline_markup(line[3:]), h2))
        elif line.startswith("- "):
            story.append(Paragraph(inline_markup(line[2:]), bullet, bulletText="•"))
        else:
            story.append(Paragraph(inline_markup(line), body))
    doc = SimpleDocTemplate(
        str(output),
        pagesize=LETTER,
        rightMargin=0.62 * inch,
        leftMargin=0.62 * inch,
        topMargin=0.62 * inch,
        bottomMargin=0.62 * inch,
        title=source.stem.replace("_", " "),
        author="Elias Leslie",
    )
    doc.build(story)


def main() -> None:
    for source, output in JOBS:
        render(source, output)
        print(f"rendered {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
