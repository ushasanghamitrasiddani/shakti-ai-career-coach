from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor


def generate_resume_pdf(resume_text, filename="resume.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title_style = styles["Heading1"]
    title_style.alignment = TA_CENTER
    title_style.textColor = HexColor("#0F4C81")

    heading_style = styles["Heading2"]
    heading_style.textColor = HexColor("#0F4C81")

    body_style = styles["BodyText"]

    story = []

    lines = resume_text.split("\n")

    first_heading = True

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Main Title
        if line.startswith("# "):
            story.append(
                Paragraph(line.replace("# ", ""), title_style)
            )
            story.append(Spacer(1, 18))

        # Section Heading
        elif line.startswith("## "):
            story.append(
                Paragraph(line.replace("## ", ""), heading_style)
            )
            story.append(Spacer(1, 8))

        # Bullet Points
        elif line.startswith("- ") or line.startswith("•"):
            story.append(
                Paragraph(f"• {line[2:]}", body_style)
            )

        # Normal Text
        else:
            story.append(
                Paragraph(line, body_style)
            )

        story.append(Spacer(1, 6))

    doc.build(story)

    return filename