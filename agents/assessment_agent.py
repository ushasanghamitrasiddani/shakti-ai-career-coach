import re


def process(text):
    """
    Formats the assessment section for better readability.
    """

    if not text:
        return "Assessment not available."

    text = text.strip()

    replacements = {
        "**Career Readiness Score:**": "## 🎯 Career Readiness Score\n",
        "**Strengths:**": "## 💪 Strengths\n",
        "**Weaknesses:**": "## 📌 Areas to Improve\n",
        "**Transferable Skills:**": "## 🔄 Transferable Skills\n",
        "**Confidence Boost:**": "## 🌟 Confidence Boost\n",
        "**Recommendation:**": "## 🚀 Recommendation\n",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text