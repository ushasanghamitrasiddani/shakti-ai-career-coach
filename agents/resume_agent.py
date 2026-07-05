import re


def process(text):
    """
    Processes and formats the Resume section.
    """

    if not text:
        return "Resume not available."

    text = text.strip()

    replacements = {
        "Professional Summary": "## 👤 Professional Summary",
        "Career Objective": "## 🎯 Career Objective",
        "Skills": "## 💼 Skills",
        "Experience": "## 💻 Experience",
        "Education": "## 🎓 Education",
        "Projects": "## 🚀 Projects",
        "Certifications": "## 📜 Certifications",
    }

    for heading, new_heading in replacements.items():

        # Replace plain headings
        text = re.sub(
            rf"^{heading}$",
            new_heading,
            text,
            flags=re.MULTILINE | re.IGNORECASE,
        )

        # Replace bold headings (**Heading**)
        text = re.sub(
            rf"\*\*{heading}\*\*",
            new_heading,
            text,
            flags=re.IGNORECASE,
        )

    # Remove extra blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text