def get_learning_path(goal):
    """
    Returns a recommended learning path based on the user's career goal.
    """

    if goal == "Software Testing":
        return [
            "Manual Testing",
            "SQL",
            "API Testing",
            "Selenium",
            "Python",
            "AI-assisted Testing"
        ]

    elif goal == "Software Development":
        return [
            "Python",
            "Data Structures",
            "Object-Oriented Programming",
            "Git & GitHub",
            "Flask / Django",
            "AI Coding Tools"
        ]

    elif goal == "Data Analytics":
        return [
            "Excel",
            "SQL",
            "Python",
            "Power BI",
            "Pandas",
            "Statistics"
        ]

    elif goal == "AI / Machine Learning":
        return [
            "Python",
            "NumPy",
            "Pandas",
            "Machine Learning",
            "Generative AI",
            "Prompt Engineering"
        ]

    elif goal == "Project Management":
        return [
            "Agile",
            "Scrum",
            "Jira",
            "Communication",
            "Leadership",
            "Risk Management"
        ]

    else:
        return [
            "Career Exploration",
            "Communication Skills",
            "LinkedIn Profile",
            "Resume Building"
        ]