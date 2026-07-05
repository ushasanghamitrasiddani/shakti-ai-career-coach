from utils.gemini_service import generate_complete_report
from agents.assessment_agent import process as assessment_process
from agents.skill_gap_agent import process as skill_gap_process
from agents.roadmap_agent import process as roadmap_process
from agents.resume_agent import process as resume_process
from agents.interview_agent import process as interview_process


def parse_report(report):
    """
    Splits the complete Gemini report into sections.
    """

    sections = {
        "assessment": "",
        "skill_gap": "",
        "roadmap": "",
        "resume": "",
        "interview": "",
    }

    current = None

    for line in report.splitlines():

        line = line.strip()

        if line == "###ASSESSMENT###":
            current = "assessment"
            continue

        elif line == "###SKILL_GAP###":
            current = "skill_gap"
            continue

        elif line == "###ROADMAP###":
            current = "roadmap"
            continue

        elif line == "###RESUME###":
            current = "resume"
            continue

        elif line == "###INTERVIEW###":
            current = "interview"
            continue

        if current:
            sections[current] += line + "\n"

    return sections

def run_career_analysis(career_profile):
    report = generate_complete_report(career_profile)

    sections = parse_report(report)

    sections["assessment"] = assessment_process(
    sections["assessment"]
 )

    sections["skill_gap"] = skill_gap_process(
    sections["skill_gap"]
)

    sections["roadmap"] = roadmap_process(
    sections["roadmap"]
 )

    sections["resume"] = resume_process(
    sections["resume"]
 )

    sections["interview"] = interview_process(
    sections["interview"]
 )

    return sections  
           
 