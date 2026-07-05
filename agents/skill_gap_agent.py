import re


def process(text):
    """
    Processes and formats the Skill Gap section.
    """

    if not text:
        return "Skill Gap Analysis not available."

    text = text.strip()

    replacements = {
        "Current Skills": "## ✅ Current Skills",
        "Required Skills": "## 🎯 Required Skills",
        "Skill Gap Analysis": "## 📊 Skill Gap Analysis",
        "Recommended Learning Order": "## 📚 Recommended Learning Order",
        "Estimated Learning Time": "## ⏳ Estimated Learning Time",
        "Practice Projects": "## 💻 Practice Projects",
        "Final Recommendation": "## 🚀 Final Recommendation",
    }

    for heading, new_heading in replacements.items():

        text = re.sub(
            rf"\*\*{re.escape(heading)}\*\*",
            new_heading,
            text,
            flags=re.IGNORECASE,
        )

        text = re.sub(
            rf"^{re.escape(heading)}$",
            new_heading,
            text,
            flags=re.MULTILINE | re.IGNORECASE,
        )

    text = re.sub(r"\n{3,}", "\n\n", text)

    return text