import re


def process(text):
    """
    Formats the learning roadmap for better readability.
    """

    if not text:
        return "Roadmap not available."

    text = text.strip()

    replacements = {
        "Learning Objective": "## 🎯 Learning Objective",
        "Phase 1": "## 📘 Phase 1",
        "Phase 2": "## 📗 Phase 2",
        "Phase 3": "## 📙 Phase 3",
        "Recommended Resources": "## 📚 Recommended Resources",
        "Weekly Milestones": "## 📅 Weekly Milestones",
        "Portfolio Projects": "## 💻 Portfolio Projects",
        "Expected Outcome": "## 🚀 Expected Outcome",
    }

    for heading, new_heading in replacements.items():

        text = re.sub(
            rf"\*\*{heading}\*\*",
            new_heading,
            text,
            flags=re.IGNORECASE,
        )

        text = re.sub(
            rf"^{heading}$",
            new_heading,
            text,
            flags=re.MULTILINE | re.IGNORECASE,
        )

    text = re.sub(r"\n{3,}", "\n\n", text)

    return text