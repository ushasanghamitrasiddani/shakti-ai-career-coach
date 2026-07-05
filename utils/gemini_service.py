import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompts.master_prompt import build_master_prompt

import streamlit as st

# Load environment variables (for local development)
load_dotenv()

# Read API key
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except Exception:
    api_key = os.getenv("GEMINI_API_KEY")
# Configure Gemini
genai.configure(api_key=api_key)

# Create the model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_career_advice(
    education,
    previous_job,
    skills,
    career_gap,
    goal,
):
    """
    Generate personalized career advice using Gemini.
    """

    prompt = f"""
You are an experienced AI Career Coach.

Candidate Details:

Education: {education}

Previous Job:
{previous_job}

Current Skills:
{skills}

Career Gap:
{career_gap} years

Career Goal:
{goal}

Provide:

1. Skill Gap Analysis

2. Personalized Learning Roadmap

3. Job Roles Suitable

4. Resume Improvement Tips

5. Interview Preparation Tips

Keep the response motivating and structured.
"""

    response = model.generate_content(prompt)

    return response.text
def ask_gemini(prompt):
    """
    Sends any prompt to Gemini and returns the response.
    """

    response = model.generate_content(prompt)

    return response.text
def generate_complete_report(career_profile):
    """
    Makes ONE Gemini call and returns the complete report.
    """

    prompt = build_master_prompt(career_profile)

    response = model.generate_content(prompt)

    return response.text