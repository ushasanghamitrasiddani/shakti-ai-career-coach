import re


def process(text):
    """
    Processes and formats the Interview section.
    """

    if not text:
        return "Interview Guide not available."

    text = text.strip()

    replacements = {
        "Technical Interview Questions": "## 💻 Technical Interview Questions",
        "HR Interview Questions": "## 👩‍💼 HR Interview Questions",
        "Behavioral Questions": "## 🧠 Behavioral Questions",
        "Career Gap Questions": "## 🌸 Career Gap Questions",
        "Sample Answers": "## ✅ Sample Answers",
        "Interview Tips": "## 🎯 Interview Tips",
        "Final Motivation": "## 🚀 Final Motivation",
    }

    for heading, new_heading in replacements.items():

        # Replace bold headings
        text = re.sub(
            rf"\*\*{re.escape(heading)}\*\*",
            new_heading,
            text,
            flags=re.IGNORECASE,
        )

        # Replace plain headings
        text = re.sub(
            rf"^{re.escape(heading)}$",
            new_heading,
            text,
            flags=re.MULTILINE | re.IGNORECASE,
        )

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text